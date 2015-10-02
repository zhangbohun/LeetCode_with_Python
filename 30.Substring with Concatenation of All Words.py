# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:55:11 2015

@author: zhangbohun
"""
'''You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).'''
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        # initialize d, l, ans
        l = len(words[0])
        d = {}#存需要匹配字符串作为键的出现次数
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        ans = []
        
        # sliding window(s),比较一段字符串
        for k in range(l):
            left = k
            subd = {}
            count = 0
            for j in xrange(k, len(s)-l+1, l):
                tword = s[j:j+l]
                # valid word，这段字符串内有没有要比较字
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + l
                    subd = {}
                    count = 0
        return ans
s=Solution()
print s.findSubstring("barfoothefoobarman",["foo", "bar"])