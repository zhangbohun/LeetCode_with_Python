# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 22:06:00 2015

@author: zhangbohun
"""
'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        first = mapping[digits[0]]
        additional = self.letterCombinations(digits[1:])
        return [s + c for s in first for c in additional]

s=Solution()
print s.letterCombinations('3245')

