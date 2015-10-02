# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:35:52 2015

@author: zhangbohun
"""
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()((),)", "()()()"
'''
class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left: generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:  parens += p,#添加字符串到list“，”的作用
            return parens
        return generate('', n, n)
s=Solution()
print s.generateParenthesis(3)