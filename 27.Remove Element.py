# -*- coding: utf-8 -*-
"""
Created on Sun Aug 02 17:54:46 2015

@author: zhangbohun
"""
'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        try:
            while 1:
                nums.remove(val)
        except:
            return len(nums)


s=Solution()
print s.removeElement([1,2,3,3],3)