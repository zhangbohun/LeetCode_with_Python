# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 18:44:52 2015

@author: zhangbohun
"""
'''
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        num1,num2,num3=0,0,0
        s1,s2=[],[]
        l4=l3=ListNode(0)
        while l1:
            s1.insert(0,l1.val)
            l1=l1.next
        while l2:
            s2.insert(0,l2.val)
            l2=l2.next
            
        for s in s1:
            num1=num1*10+s
        for s in s2:
            num2=num2*10+s
            
        num3=num1+num2#化繁为简
        
        if num3<10:
            l3.val=num3
        while num3/10:
            l3.val=num3%10
            num3=num3/10
            if num3/10:
                l3.next=ListNode(0)
                l3=l3.next
            else:
                l3.next=ListNode(num3)
        
        return l4