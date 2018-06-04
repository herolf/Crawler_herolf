# coding: utf-8
 
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
import requests
import re
from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag
def getHtml(url):
    try:
        html = requests.get(url)
        bsObj = BeautifulSoup(html.text,'lxml')
        Html = bsObj
    except AttributeError as e:
        return None
    return Html
url="https://www.bitask.org/question/8560"
html = getHtml(url)

asker_head=html.body.find('dd',class_='pull-left')

if asker_head != None :
    asker_name=asker_head.a.string
else :
    asker_name=None
question_region=html.body.find_all(class_='aw-mod aw-question-detail aw-item')
times=0
question_title_string=None
question_content_list = []
for i in question_region:
    if times==0:                    
        question_title          = i.h1.contents
        question_title_Nstring  = question_title[0].string                                                
        question_title_string   = str(question_title_Nstring).strip()
        question_contents=i.find_all(text=re.compile(''))
        ii_times=0
        for ii in question_contents:
            if ii_times>=1 and re.match(r'<',ii)==None and ii!=" 站内邀请 " and ii != " end 站内邀请 " and ii !="没有找到相关结果" and ii != "与内容相关的链接" and ii != "&yen; 打赏"\
            and ii != " "  and  ii != "添加评论" and ii != "置顶" and ii !="分享\t\t\t\t\t\t\t\t\t" and ii != " 相关链接 " and ii != " end 相关链接 " and ii != "提交" and ii !="\n"\
            and re.match(r'^ <',ii)==None and re.search(ur'转账|已邀请',ii.decode('utf-8'))==None:
                ii=unicode(ii)
                question_content_list.append(ii)
                print ii 
            ii_times+=1
print  asker_name
print  question_title_string
#回答区域

answers_head=html.body.find(class_="mod-body aw-feed-list")
if answers_head is  None:
    print ("Error,answers_head is  None!Please check!")
else:
    answer=answers_head.find(class_="aw-item")
print ("==========================================+++++++++++++++++++++++++++++++++++++++++++++++++++++")
flag=1
while answer!=None:                                                                     
    if (isinstance(answer,Tag)):
        #"问题标识  answer_id"
        answer_id = answer.get('id')
        print type(answer_id.decode('utf-8'))
              
        #内容 answer_content
        answer_contents=answer.find(class_="mod-body clearfix")#answer.find_all(text=re.compile(''))#answer.div[1].div.find_all(text=re.compile(''))
        answer_contenttemp=answer_contents.get_text().split('\n')                         #.content方法会导致带着所有标签  .get_text方法导致所有的文章没有换行符
        #print type(answer_contenttemp)
        #print (answer_contenttemp.strip())
        #answer_content=answer_contenttemp.strip()                           
        print answer_contenttemp
        #回答者：answer_man
        answer_man=answer.find(class_="aw-user-name").get_text().strip()
        print answer_man
        #点赞者：voter_list
        answer_voters=answer.find(class_="text-color-999 aw-agree-by")
        #print type(answer_voters)
        if (isinstance(answer_voters,Tag)):
            answer_voter_search=answer_voters.find_all(class_="aw-user-name")

        voter_list=[]
        for answer_voter in answer_voter_search:
            
            voter_list.append(answer_voter.get_text())
            print answer_voter.get_text()
        print (u"回答结束========================================================================================================================================================")
    #else:
        #print ("未找到符合需求的标签，进入下一步")
    answer = answer.next_sibling
    flag+=1


    








        #if (re.match(r'<',ii)) == None  and ii != " " and ii !="\n" and ii!="\n、" and ii!="、" and re.search(ur'社交操作|分享|用户头像|可显示|投票栏',ii.decode('utf-8'))==None :
            #print ii 