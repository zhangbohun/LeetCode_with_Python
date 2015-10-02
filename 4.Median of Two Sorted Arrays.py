# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 18:50:29 2015

@author: zhangbohun
"""
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively. 
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        C=A+B
        C.sort()
        if len(C)<=2:
            if len(C)==2:
                return (C[0]+C[1])/2.0
            else:
                return C[0]
        if len(C)%2:
          return C[len(C)/2]  
        else:
            return (C[len(C)/2-1]+C[len(C)/2])/2.0

s=Solution()
print s.findMedianSortedArrays([1,2,3,4,5],[3,6,8,9,16])