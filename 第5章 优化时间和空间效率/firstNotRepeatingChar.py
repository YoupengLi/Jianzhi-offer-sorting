# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 0024 上午 11:16
# @Author  : Youpeng Li
# @Site    : 
# @File    : FirstNotRepeatingChar.py
# @Software: PyCharm

'''
题目：在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置

思路：先遍历一遍字符串，用一个hash表存放每个出现的字符和字符出现的次数。再遍历一遍字符串，找到hash值等于1的输出即可。
'''

class Solution:
    def firstNotRepeatingChar(self, s: 'str') -> 'int':
        if not s or len(s) <= 0:
            return -1

        char_dict = {}
        for i in s:
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
        for ind, val in enumerate(s):
            if char_dict[val] == 1:
                return ind
        return -1

if __name__ == "__main__":
    a = Solution()
    s = "abaccdeff"
    print(a.firstNotRepeatingChar(s))