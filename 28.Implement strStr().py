# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 20:01:43 2015

@author: zhangbohun
"""
'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        i = 0
        while len(haystack[i:])>=len(needle):
            if needle==haystack[i:i+len(needle)]:
                return i
            i+=1
        return -1
s=Solution()
print s.strStr('abvs','vs')



