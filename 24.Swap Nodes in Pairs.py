# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:23:17 2015

@author: zhangbohun
"""
'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        p=q=head
        if head==None:#没有
            return head
        if head.next==None:#一个
            return head
        if head.next.next==None:#两个
            p.val,p.next.val=p.next.val,p.val
            return head
        p.val,p.next.val=p.next.val,p.val
        q=p.next
        while q.next!=None:#偶数个
            p=q.next
            if p.next==None:#奇数个
                return head
            else:
                p.val,p.next.val=p.next.val,p.val
                q=p.next
        return head


