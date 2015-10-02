# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 19:21:22 2015

@author: zhangbohun
"""
'''
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
    # @return a string
    def intToRoman(self, num):
        units=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        decade=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hundred=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        kilobit=["","M","MM","MMM","MMMM"]
        return kilobit[num/1000]+hundred[(num/100)%10] +decade[(num/10)%10]+units[num%10]

s=Solution()
print s.intToRoman(122)