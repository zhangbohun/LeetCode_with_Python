# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 18:48:24 2015

@author: zhangbohun
"""
'''
Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s)!=0:
            str1=[s[0]]
            str2=str1[:]
            i=0
            while i+1 <len(s):
                if s[i+1] not in str1:
                    str1.append(s[i+1])
                    if len(str2)<len(str1):
                        str2=str1[:]
                    i+=1
                else:
                    str1.pop(0)
            return len(str2)
        else:
            return 0
s=Solution()
print s.lengthOfLongestSubstring('abcabcbb')