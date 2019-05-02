# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 16:58
# @Author  : Youpeng Li
# @Site    : 
# @File    : isAnagram.py
# @Software: PyCharm

'''
题目：在英语中，如果两个单词出现的字母相同，并且每个字母出现的次数也相同，那么这两个单词互为变位词(Anagram)。
例如，silent与listen、evil与live等互为变位数。请完成一个函数，判断输入的两个字符串是不是互为变位词。

解题思路：创建一个用数组实现的简单哈希表，用来统计字符串中每个字符出现的次数。当扫描到第一个字符串的每个字符时，为哈希表对应的项的值增加1。
接下来扫描第二个字符串，扫描到第二个字符时，为哈希表对应的项的值减去1。
如果扫描完第二个字符串后，哈希表中所有的字符串都是0，那么这两个字符串就互为变位词。
'''

class Solution:
    def isAnagram(self, s1: 'str', s2: 'str') -> 'bool':
        if not s1 or len(s1) <= 0 or not s2 or len(s2) <= 0:
            return False
        if len(s1) != len(s2):
            return False
        dict1 = {}
        for i in s1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        for i in s2:
            if i not in dict1:
                return False
            else:
                dict1[i] -= 1
        for i in dict1.keys():
            if dict1[i] != 0:
                return False
        return True

if __name__ == "__main__":
    a = Solution()
    s1 = "silent"
    s2 = "listen"
    print(a.isAnagram(s1, s2))