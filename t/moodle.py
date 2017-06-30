# -*- coding:UTF-8 -*-
'''
Created on 2016年10月1日

@author: Administrator
'''
from Cookie import Cookie
from bs4 import BeautifulSoup
import cookielib
import urllib2
import urllib
from types import NoneType
from course import courseclass
import time
hosturl = 'http://moodle.hstc.edu.cn/'
posturl = 'http://moodle.hstc.edu.cn/login/index.php'


cj=cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)

h = urllib2.urlopen(hosturl)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',  
           'Referer' : 'http://moodle.hstc.edu.cn/login/index.php'}  

postData={
    'username' : '2014115106',
    'password' : 'weisheng',
    'anchor':''
    }
postData=urllib.urlencode(postData)

request = urllib2.Request(posturl,postData,headers)
response=urllib2.urlopen(request)
text = response.read()
soup = BeautifulSoup(text,'html.parser',from_encoding='uft-8')
link = soup.find('a', title = '我的课程')
url=link['href']
print(url)
responsemy=urllib2.urlopen(url)
my=responsemy.read()
soup = BeautifulSoup(my,'html.parser',from_encoding='uft-8')
extend=soup.find('div',class_='box notice')
if extend != None:
    getextend=extend.a['href']
    responsemy=urllib2.urlopen(getextend)
    my=responsemy.read()
    soup = BeautifulSoup(my,'html.parser',from_encoding='uft-8')
    
course_list = soup.findAll('div',class_="box coursebox")

courselist = list()
for link in course_list:
    c=courseclass()
    c.setname(link.find('a').get_text())

    zy=link.find('a',title='作业')
    if zy != None:
        c.sethomework(zy.get_text())

    lt=link.find('div',class_='info')
    if lt != None:
        c.setddl(lt.get_text())
#         截止时间: 2016年10月10日 星期一 00:00
#         time.strptime(,'%Y年%m月%日 星期一 %H:%M:%S')
    if  (c.name!='') and (c.homework!='') and (c.ddl!=''):
        courselist.append(c)
        
for c1 in courselist:
    print(c1.name)
    print(c1.homework)
    print(c1.ddl)
    
    
    
    