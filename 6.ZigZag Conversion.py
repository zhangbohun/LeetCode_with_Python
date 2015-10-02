# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 19:08:05 2015

@author: zhangbohun
"""
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution:
    # @return a string
    def convert(self, s, nRows):
        i=0
        str=''
        if nRows==1 or s=='':
            return s
        str=str +s[i::2*nRows-2]
        i+=1
        while i < nRows-1 and i<len(s)-1:
            str+=s[i]
            j=i
            while j+2*nRows-2*(i+1) <=len(s)-1:
                str+=s[j+2*nRows-2*(i+1)]
                if j+2*nRows-2<=len(s)-1:
                    str+=s[j+2*nRows-2]
                j+=2*nRows-2
            i+=1
        str=str +s[i::2*nRows-2]
        return str

s=Solution()
print s.convert("PAYPALISHIRING", 3)