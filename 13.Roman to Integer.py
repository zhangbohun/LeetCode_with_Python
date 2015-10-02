# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 19:22:26 2015

@author: zhangbohun
"""
'''
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
    # @return an integer
    def romanToInt(self, s):
        str = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        num=0
        while i<len(s):
            if i+1<len(s):
                if (s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X') ) \
                    or (s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C')) \
                    or (s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M')):
                    num-=str[s[i]]
                else:
                    num +=str[s[i]]
            else:
                num +=str[s[i]]
            i+=1
        return num

s=Solution()
print s.romanToInt("XX")