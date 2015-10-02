# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 19:32:49 2015

@author: zhangbohun
"""
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
For example, given array S = {-1 0 1 2 -1 -4},

A solution set is:
(-1, 0, 1)
(-1, -1, 2)
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if len(nums) <3: # deal with special input
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]

        nums = sorted(nums) # sorted, O(nlgn)
        ans = []

        for i in range(len(nums) -2):
            j = i+1
            k = len(nums) -1 # hence i < j < k

            while j<k: # if not cross line
                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum == 0:
                    ans.append((nums[i], nums[j], nums[k]))

                if temp_sum > 0: # which means we need smaller sum, move k backward, remember we sort the array
                    k -= 1
                else:
                    j += 1

        return list(set(tuple(ans))) # I bet this is not the best way to eliminate duplicate solutions

s=Solution()
print s.threeSum([-1,0,1,2,-1,-4])