#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:44:54 2020

@author: liwei
"""
number = int(input("Input a number: "))
temp = 0

for i in range(1, number+1):
    if(i % 15 == 0):
        temp += 1 #3與5最小倍數為15 凡被除於數為零則為他的倍數
    elif(i % 3 == 0 or i % 5 ==0):
        continue #jump out the loop
    
    else:
        temp += 1
        
print(temp)