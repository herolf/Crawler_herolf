# coding: utf-8
import json
import re


def sort_dict(dict):
    sort_dict = []
    #print(len(dict))
    all_vote=0
    for i in range(len(dict)):
        flag=0
        max=0
        
        for key,value in dict.items() :
            if flag == 0:
                max=int(value)
                temp=key
                flag +=1
            elif int(value) > max:
                max=int(value)
                temp=key
                flag +=1
        sort_dict.append({temp:max})
        dict.pop(temp)
        all_vote+=max
    sort_dict.append({"总点赞数":all_vote})
    #print (sort_dict)
    return (sort_dict)


list_sort=[]
with open ('votersdict.txt','r',encoding='utf-8') as f:
    dict_str=f.read()
    dict_str=re.sub('[\'|\"]','\"',dict_str)  
    dict_dict=json.loads(dict_str)
    dict=sort_dict(dict_dict)
    #print (type(dict_str))
    print (dict)


'''
with open ('votersdict.txt','r',encoding='utf-8') as f:
    dict_str=f.read()
    dict_str=re.sub('[\'|\"]','\"',dict_str)  
    dict_dict=json.loads(dict_str) 
    print (type(dict_str))
    print ((dict_dict))
    for key,value in dict_dict.items():
        if list_sort == []:
           list_sort.append({key:value})
           #print (list_sort[0][key])
    
        else :
            flag=0
            for i in len(list_sort):
                if flag==0:
                    if value<=list_sort[i][key]:
                        flag=i
                    else:
                        flag=0
                elif (value <= i[key]):

                    flag = i
                    
    print (list_sort)
'''

