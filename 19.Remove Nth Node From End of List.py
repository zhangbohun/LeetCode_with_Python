# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:50:40 2015

@author: zhangbohun
"""
'''
Given a linked list, remove the nth node from the end of list and return its head.
For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        p1=p2=p3=head
        if head.next==None:
            return []
        for i in range(0,n-1):
            p3=p3.next
        while p3.next!=None:
            p3=p3.next
            p1=p2
            p2=p2.next
        #关键在于链表的头和尾处理
        if p1 ==p2:
            head=head.next
            return head
        if p2.next!=None:
            p1.next=p2.next
        else:
            p1.next=None
        return head