# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 18:41:35 2015

@author: zhangbohun
"""
'''
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dic={}
        for i in range(len(num)):
            if num[i] not in dic:#这里是关键,哈希
                dic[target-num[i]]=i+1
            else:
                return dic[num[i]],i+1
s=Solution()
print s.twoSum([2,7,11,15],9)