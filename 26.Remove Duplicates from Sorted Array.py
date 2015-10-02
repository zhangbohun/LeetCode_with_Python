# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:24:58 2015

@author: zhangbohun
"""
'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the new length.
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        end = len(nums)-1
        while(end > 0):
            if(nums[end] == nums[end-1]):
                nums.pop(end)
            end-=1
        return len(nums)

s=Solution()
print s.removeDuplicates([1,1,2,2,3,4])
