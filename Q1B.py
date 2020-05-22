#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:44:12 2020

@author: liwei
"""
def reverse_sentence(s):
    string_list = s.split(' ')
    for i in range(len(string_list)):
        string_list[i] = string_list[i][::-1] # same as reverse_single
        
    return ' '.join(string_list)    
a2 = input('Input a sentence to reverse each string but not sentence order: ')
print(reverse_sentence(a2))  