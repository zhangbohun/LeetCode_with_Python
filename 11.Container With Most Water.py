# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 19:18:30 2015

@author: zhangbohun
"""
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''

class Solution:
    # @return an integer
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        bigger=0
        while i<j:
            bigger = max([bigger,min([height[i],height[j]])*(j-i)])
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return bigger

s=Solution()
print s.maxArea([1,2,4,3,6])