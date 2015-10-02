# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:08:10 2015

@author: zhangbohun
"""
'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        # use timsort O(n)
        nodes = []
        for head in lists:
            while head:
                nodes.append(head)
                head = head.next
    
        if not nodes:
            return
    
        nodes.sort(key=lambda x: x.val)#用lambda匿名函数实现排序
    
        for i in xrange(1, len(nodes)):#重新做成list
            nodes[i-1].next = nodes[i]
    
        nodes[-1].next = None
        return nodes[0]