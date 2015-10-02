# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:51:48 2015

@author: zhangbohun
"""
'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        l=ListNode(None)
        p=l1
        q=l2
        r=l
        if p==None:
            return q
        if q==None:
            return p
        #处理头和尾是关键
        while p!=None and q !=None:
            if p.val<q.val:
                r.val=p.val
                p=p.next
                r.next=ListNode(None)
                r=r.next
            else:
                r.val=q.val
                q=q.next
                r.next=ListNode(None)
                r=r.next
        if q!=None:
            r.val=q.val
            r.next=q.next
        elif p!=None:
            r.val=p.val
            r.next=p.next
        return l
        
s=Solution()
#print s.mergeTwoLists()