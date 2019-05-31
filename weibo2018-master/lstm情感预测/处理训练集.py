# encoding: utf-8
from pyecharts import Pie

from lstm情感预测.Sentiment_lstm import lstm_predict

with open('test.txt','r+',encoding='utf-8') as f:
    tmp_all=f.readlines()

type_list=['ture','false']
count_list=[0,0]


for i in tmp_all:
    tmp_text=i.split(',')[2]
    tmp_label=i.split(',')[1]
    #0消极1积极
    pre_label=lstm_predict(tmp_text)
    print('##'+str(pre_label))
    if int(pre_label)==int(tmp_label):
        count_list[0]+=1
    else:
        count_list[1] += 1

print(type_list)
print(count_list)

pie = Pie("snow_nlp饼图",width=500,height=300)
pie.add("", type_list, count_list, is_label_show=True)  # 第一个是名字，第二个是value值
pie.render('lstm_result.html')