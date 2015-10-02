# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:49:28 2015

@author: zhangbohun
"""
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        helper=ListNode(0)#加一个头
        helper.next=head
        q=helper
        p=head
        stack=[]

        while p!=None :
            if len(stack)==k:
                while len(stack)>0:
                    q.next=stack.pop()#倒出
                    q=q.next
                q.next=p
            else:
                stack.append(p)#装入
                p=p.next

        if len(stack)==k:#最后部分处理
            while len(stack)>0:
                q.next=stack.pop()
                q=q.next
            q.next=p
        elif len(stack)>0:
            q.next=stack[0]#剩余部分
            
        return helper.next



