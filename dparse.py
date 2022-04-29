### ВАЖНО - пока модуль работает только через hh.api
## в новой версии разрабатывается поддрежка парсинга с зарплата.ру

# Библиотека для работы с HTTP-запросами. Будем использовать ее для обращения к API HH
import requests
import json
import time
import os

def getPage(page = 0,vac_name = "Программист",sity = 47):
    #page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
    # Справочник для параметров GET-запроса
    params = {
        'text': 'NAME:'+vac_name, # Текст фильтра. В имени должно быть слово "vac_name"
        'area': sity, #id90 - Кемерово
        'page': page, # Индекс страницы поиска на HH
        'per_page': 100 # Кол-во вакансий на 1 странице
    }
    req = requests.get('https://api.hh.ru/vacancies', params) # Посылаем запрос к API
    data = req.content.decode() # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data
 
def savePage(end_range = 20):
# Считываем первые 2000 вакансий
    for page in range(0, end_range):
    # Преобразуем текст ответа запроса в справочник Python
        jsObj = json.loads(getPage(page,vac_name = "Программист"))
        nextFileName = 'docs/pages/page{}.json'.format(page+1)
    # Создаем новый документ, записываем в него ответ запроса, после закрываем
        f = open(nextFileName, mode='w', encoding='utf8')
        f.write(json.dumps(jsObj, ensure_ascii=False))
        f.close()
    # Проверка на последнюю страницу, если вакансий меньше 2000
        if (jsObj['pages'] - page) <= 1:
            break
    # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
        time.sleep(0.5)
    print('Страницы поиска собраны')

def saveFile(f_path ='/docs/pages/page1.json'):
    f = open(f_path,encoding='utf8')
    jsonText = f.read()
    print("Загружен")
    f.close()
# Преобразуем полученный текст в объект справочника
    jsonObj = json.loads(jsonText)
# Получаем и проходимся по непосредственно списку вакансий
    for v in jsonObj['items']:

# Обращаемся к API и получаем детальную информацию по конкретной вакансии
# Обрабатываем ошибки подключения, восстанавливаем соединение
### ПЕРЕДЕЛАТЬ
        try:
            req = requests.get(v['url'])
            data = req.content.decode()
            req.close()
        except requests.exceptions.ConnectionError:
            print("Проблемы соединения")
            continue
        finally:
            fileName = 'scripts/Парсер/docs/vac/vacID{}.json'.format(v['id'])
            f = open(fileName, mode='w', encoding='utf8')
            f.write(data)
            f.close()
            time.sleep(0.025)
        print("Создан",fileName)
    print('Вакансии собраны')