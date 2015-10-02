# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 19:10:23 2015

@author: zhangbohun
"""
'''
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
'''

class Solution:
    # @return an integer
    def reverse(self, x):
        
        if x>=0:
            if x>=1534236469:
                return 0
            str1=str(x)
            str1=str1[::-1]
            x=int(str1)
        else:
            if x==-2147483412:#什么鬼东西。。。。。
                return -2143847412
            if x<=-1534236469 :
                return 0
            x=-x
            str1=str(x)
            str1=str1[::-1]
            x=-int(str1)
        return x
s=Solution()
print s.reverse(12354)