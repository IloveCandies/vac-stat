import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

#Выбор датафрейма и столбца для анализа
def get_word_stat(data_url = 'data.csv',name_column ='skill_name'):
    vectorizer = CountVectorizer()
    dataset = pd.read_csv(data_url)
    skills = dataset[name_column].values.tolist()
    bag = vectorizer.fit_transform(skills)
    #print(vectorizer.vocabulary_)
    #подсчет колличество повторений слова в документе
    out_data = vectorizer.vocabulary_
    return out_data

#print(get_word_stat(data_url='web/dash/skills.csv'))