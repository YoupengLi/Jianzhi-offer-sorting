# -*- coding: utf-8 -*-
# @Time    : 2019/2/7 0007 上午 12:03
# @Author  : Youpeng Li
# @Site    : 
# @File    : leftRotateString.py
# @Software: PyCharm

'''
题目：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
例如，输入字符串"abcdefg"和数字2，该函数将返回左旋转2位得到的结果"cdefgab"。

题目：汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列s，请你把其循环左移K位后的序列输出。例如，字符序列s=”abcXYZdef”,要求输出循环左移3位后的结果，
即“XYZdefabc”。
解题思路：三次翻转法
'''

class Solution:
    def leftRotateString(self, s: 'str', n: 'int') -> 'str':
        if not s or len(s) <= 0:
            return ""
        if len(s) <= n:
            return s

        s = list(s)
        listTemp = []
        listTemp.append(self.reverse(s[0:n]))
        listTemp.append(self.reverse(s[n:]))
        return ''.join(self.reverse(sum(listTemp, [])))

    def reverse(self, s: 'list[char]') -> 'list[char]':
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s

if __name__ == "__main__":
    s = "abcdefg"
    a = Solution()
    res = a.leftRotateString(s, 2)
    print(res)