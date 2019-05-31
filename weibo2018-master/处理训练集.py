# encoding: utf-8
with open('train.txt','r+',encoding='utf-8') as f:
    tmp_all=f.readlines()

for i in tmp_all:
    tmp_text=i.split(',')[2]
    tmp_label=i.split(',')[1]

