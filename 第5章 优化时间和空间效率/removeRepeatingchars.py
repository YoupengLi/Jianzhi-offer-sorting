# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 16:39
# @Author  : Youpeng Li
# @Site    : 
# @File    : removeRepeatingchars.py
# @Software: PyCharm

'''
题目：删除字符串中所有重复出现的字符。
例如，输入”google”，则删除重复字符之后的结果是”gole”
'''

class Solution:
    def removeRepeatingchars(self, s: 'str') -> 'str':
        if not s or len(s) <= 0:
            return s
        res = [True] * len(s)
        dict1 = {}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1
                res[i] = False
        s1 = []
        for i in range(len(res)):
            if res[i]:
                s1 += s[i]
        return ''.join(s1)

if __name__ == "__main__":
    a = Solution()
    s = "google"
    print(a.removeRepeatingchars(s))