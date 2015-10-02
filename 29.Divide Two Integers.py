# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 15:56:00 2015

@author: zhangbohun
"""
'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''
class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

s=Solution()
print s.divide(108,2)



