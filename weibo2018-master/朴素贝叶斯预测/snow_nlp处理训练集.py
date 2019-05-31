# encoding: utf-8
'''
LstmPython3.6snow_nlp处理训练集 
Administrator2019/5/31 17:32 
PyCharm 五月 
'''
from snownlp import SnowNLP

import pyecharts
from pyecharts import Pie
with open('test.txt','r+',encoding='utf-8') as f:
    tmp_all=f.readlines()

type_list=['ture','false']
count_list=[0,0]


for i in tmp_all:
    tmp_text=i.split(',')[2]
    tmp_label=i.split(',')[1]
    #0消极1积极

    s = SnowNLP(tmp_text)

    # print (u'情感值：%s' % s.sentiments)

    if s.sentiments > 0.5:
        # print (u'情感分析：积极')
        ans = 1
    elif s.sentiments <= 0.5:
        # print (u'情感分析：消极' )
        ans = 0

    if ans==int(tmp_label):
        count_list[0]+=1
    else:
        count_list[1] += 1

print(type_list)
print(count_list)

pie = Pie("snow_nlp饼图",width=500,height=300)
pie.add("", type_list, count_list, is_label_show=True)  # 第一个是名字，第二个是value值
pie.render('snow_nlp_result.html')

