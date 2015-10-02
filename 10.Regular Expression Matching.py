# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 19:16:43 2015

@author: zhangbohun
"""
'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]#设置并初始化dp数组
        dp[0][0] = True #如果都为空则匹配
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'     #处理第一列*前字母0次匹配跳过情况
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    #表示*前字母0次匹配跳过的操作，如果*前字母前一次比较是不匹配的话就看再前面一个字母的匹配情况了
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':     #*表示重复前面的字母时的操作
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')#不是*时的操作
        return dp[-1][-1]

s=Solution()
print s.isMatch("aab", "c*a*b")