# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 16:22
# @Author  : Youpeng Li
# @Site    : 
# @File    : removeCharsInSecondString.py
# @Software: PyCharm

'''
题目：
输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。
例如，输入”They are students.”和”aeiou”，
则删除之后的第一个字符串变成”Thy r stdnts.”
'''

class Solution:
    def removeCharsInSecondString(self, s1: 'str', s2: 'str') -> 'str':
        if not s1 or len(s1) <= 0 or not s2 or len(s2) <= 0:
            return s1
        for i in s2:
            s1 = s1.replace(i, '')
        return s1

if __name__ == "__main__":
    a = Solution()
    s1 = "They are students."
    s2 = "aeiou"
    print(a.removeCharsInSecondString(s1, s2))