
# -*- coding:UTF-8 -*-
'''
Created on 2016年10月6日

@author: Administrator
'''
class courseclass:
    name =''
    homework = ''
    ddl = ''
    def __init__(self):
       self.ddl=''
       self.homework=''
       self.name=''
    def setname(self,name):
        self.name = name
    def sethomework(self,hw):
        self.homework = hw
    def setddl(self,ddl):
        self.ddl = ddl
    def getname(self):
        return self.name
    def gethomework(self):
        return self.homework
    def getddl(self):
        return self.ddl
