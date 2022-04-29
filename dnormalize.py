import pandas as pd

#### Не нормализованный список требованний
def non_normalize(url = 'skills.csv'):
    df = pd.read_csv(url)
    skills = df['skill_name'].values.tolist()
    result = {skill: skills.count(skill) for skill in skills if skills.count(skill) >= 1}
    return result

#Простая нормализация  необходимо чтобы элементы списков имели одинаковые индексы
### в бущем будет заменена на TF - IDF метрики 
def normalize(url = 'skills.csv',words_to_split= [], split_words = [],):
    df = pd.read_csv(url)
    skills = df['skill_name'].values.tolist()
    for skill in skills:
        if skill in words_to_split:
            skill = split_words.index(skill)
    result = {skill: skills.count(skill) for skill in skills if skills.count(skill) >= 1}
    return

#зарплаты (пока не работает как надо)
def normalize_slr(slr_url = 'salary-ranges.csv'):
    df = pd.read_csv(slr_url)
    slr_ranges= df['range'].tolist()
    result = {slr_range: slr_ranges.count(slr_range) for slr_range in slr_ranges}
    return result
