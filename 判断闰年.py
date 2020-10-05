# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:34:32 2020

@author: 洪笑笑
"""

input_year = int(input('请输入一个年份，判断是否是闰年:'))

active = 1
while active:
    if (input_year%400==0) or (input_year%4==0 and input_year% 100!=0):
        print(str(input_year)+'是闰年')
        break
              
    else:
        print(str(input_year)+'不是闰年')
        break