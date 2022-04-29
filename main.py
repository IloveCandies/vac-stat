import dparse
import dwrite
import dnormalize
import plotly.express as px
import pandas as pd
#dparse.savePage()
#dwrite.data_to_csv()

result = dnormalize.non_normalize()
pr_result = {}
count = 0

# Отображение проценов
for val in result.values():
    count += val
precent_val = count/100

for item in result.items():
    prec = item[1]/precent_val
    pr_result[item[0]] = round(prec,2)


salary = dnormalize.normalize_slr()

#Графики
out =  pd.DataFrame(result.items(),columns = ['Название языка, средства или технологии программирования','Колличество упоминаний в требованиях'])
out.to_csv('out4.csv')

#fig = px.bar(out, x = 'Название языка, средства или технологии программирования', y = 'Колличество упоминаний в требованиях') 
#fig.show()

#out =  pd.DataFrame(pr_result.items(),columns = ['Название языка, средсва или технологии','Процент упоминаний в требованиях'])
#fig = px.bar(out, x = 'Название языка, средсва или технологии', y = 'Процент упоминаний в требованиях') 
#fig.show()

#out =  pd.DataFrame(salary.items(),columns = ['Зарплата','Колличество упоминаний'])
#fig = px.bar(out, x = 'Зарплата', y = 'Колличество упоминаний') 
#fig.show()