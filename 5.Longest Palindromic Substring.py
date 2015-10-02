# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 19:01:43 2015

@author: zhangbohun
"""
'''
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        t = '^#'+'#'.join(s) +'#%'
        p=[0]*len(t)
        center=border=0
        for i in range(1,len(t)-1):
            if border > i:
                p[i] = min(border - i, p[2*center - i])#对称范围内的字符的两边的对称情况相同
            else:
                p[i] = 0
            while t[i+1+p[i]] == t[i-1-p[i]]:
                p[i] += 1
            if i + p[i] > border:
                center, border = i, i + p[i]
        
        maxLen, centerIndex = max((n, i) for i, n in enumerate(p))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]#t下标除以二正好是s对应的下标
        
s=Solution()
print s.longestPalindrome('sdgfsdgfsdsssdsdfsdfds')