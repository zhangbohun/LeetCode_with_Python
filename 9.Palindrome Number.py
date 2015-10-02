# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 19:14:30 2015

@author: zhangbohun
"""
'''
Determine whether an integer is a palindrome. Do this without extra space.
'''
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]

s=Solution()
print s.isPalindrome(121)