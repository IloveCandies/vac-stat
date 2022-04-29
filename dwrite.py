import pandas as pd
import plotly.express as px
import json
import os


def data_to_csv(dir_path = '/docs/vac'):
    # Создаем списки для столбцов таблицы vacancies
    IDs = [] # Список идентификаторов вакансий
    names = [] # Список наименований вакансий
    descriptions = [] # Список описаний вакансий
    all_skills = []
    salary = []
    # Создаем списки для столбцов таблицы skills
    skills_vac = [] # Список идентификаторов вакансий
    skills_name = [] # Список названий навыков
    # В выводе будем отображать прогресс
    # Для этого узнаем общее количество файлов, которые надо обработать
    # Счетчик обработанных файлов установим в ноль
    cnt_docs = len(os.listdir(dir_path))
    i = 0
    # Проходимся по всем файлам в папке vacancies
    for fl in os.listdir(dir_path):
    # Открываем, читаем и закрываем файл
        f = open('{0}/{1}'.format(dir_path,fl), encoding='utf8')
        print(fl) #дебаг принтами еееееееееее
        jsonText = f.read()
        f.close()
        # Текст файла переводим в справочник
        jsonObj = json.loads(jsonText)
    # Заполняем списки для таблиц
        IDs.append(jsonObj['id'])
        names.append(jsonObj['name'])
        descriptions.append(jsonObj['description'])
    # Т.к. навыки хранятся в виде массива, то проходимся по нему циклом
        allsk =""
        for skl in jsonObj['key_skills']:
            skills_vac.append(jsonObj['id'])
            skills_name.append(skl['name'])
            allsk += skl['name']+"|"
        all_skills.append(allsk)
        i += 1
        salary.append(jsonObj['salary'])

    #Сохраняем в CSV     
    df = pd.DataFrame({'id': IDs, 'name': names, 'skill':all_skills,'description': descriptions})
    df.to_csv('vacancies.csv',index=False)
    df = pd.DataFrame({'skill_name':skills_name,'skill_vac':skills_vac,})
    df.to_csv('skills.csv',index=False)
    df = pd.DataFrame({'range':salary})
    df.to_csv('salary-ranges.csv',index=False)

