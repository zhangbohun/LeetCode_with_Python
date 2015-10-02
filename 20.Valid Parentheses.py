# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:17:14 2015

@author: zhangbohun
"""
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        t=[]#用栈来处理括号
        for i in s:
            if i in ['(','[','{']:
                t.append(i)
            if i==')':
                if not len(t):
                    return False
                elif t[-1] in['[','{']:
                    return False
                else:
                    t.pop()
            if i==']':
                if not len(t):
                    return False
                elif t[-1] in ['(','{']:
                    return False
                else:
                    t.pop()
            if i=='}':
                if not len(t):
                    return False
                elif t[-1] in ['[','(']:
                    return False
                else:
                    t.pop()
        if not len(t):
            return True
        else:
            return False
s=Solution()
print s.isValid("[()()]")