# coding: utf-8

from bson.objectid import ObjectId
import requests
import re
from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag

from pymongo import MongoClient
import pprint
import pymongo
#数字到日期的格式化
def numtodate(num):
    ma=re.match(r'([0-9]{4})([0-9]{2})([0-9]{2})',num)
    year=ma.group(1)
    month=ma.group(2)
    day=ma.group(3)
    date=str(year)+'-'+str(month)+'-'+str(day)
    return date




def get_db(db_name):
    #setup
    client = MongoClient("localhost",27017)
    db=client[db_name]
    return db

def get_collection(db,collection_name):
    coll=db[collection_name]
    return coll

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
    #sort_dict.append({"总点赞数":all_vote})
    #print (sort_dict)
    return (sort_dict)



def get_answers_voters(answers_name,answers_collect,list,dict):
    answer_man=answers_name
    search_answers={"answer_man":answer_man}
    docs= answers_collect.find(search_answers)

    times=0
    emptimes=0
    #voter count and list #所有点赞人：点赞数
    for doc in docs:
        a=pprint.pprint(doc["voter_list"])
        a=doc["voter_list"]
        if a == [] :
            emptimes+=1
        for i in a:
            flag=0
            for ii in list:
                if ii==i:
                    flag+=1
                    dict[i]+=1
                    continue
            if flag==0:
                list.append(i)
                dict[i]=1
        times +=1
    print (list)
    print (dict)
    print (emptimes)
    print (times)
    print (len(list))
    dict1=sort_dict(dict)
    return dict1
list=[]
dict={}
db=get_db("biask")
ask=get_collection(db,"ask_region")
answers=get_collection(db,"answers_region")

a=get_answers_voters("橡皮擦",answers,list,dict)
print (a)
#get_answers_voters(,answers,list,dict)
#answer_man=answers_name
#search_answers={"answer_man":answer_man}



#统计所有文章数量
#contents
#list=[]
#dict={}


