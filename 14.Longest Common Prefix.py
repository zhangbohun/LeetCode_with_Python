# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 19:23:40 2015

@author: zhangbohun
"""
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution:
    # @param {string[]} strs
    # @return {string}
    #题意为所有字符串的公共子串
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        str = strs[0]
        res = ''
        for i in range(len(str)):
            for j in range(1,len(strs)):
                if i > len(strs[j]) - 1:
                    return res
                if str[i] != strs[j][i]:
                    return res
            res += str[i]
        return res

s=Solution()
print s.longestCommonPrefix(['we','wegfh'])