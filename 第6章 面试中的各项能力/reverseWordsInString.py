# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 8:18
# @Author  : Youpeng Li
# @Site    : 
# @File    : reverseWordsInString.py
# @Software: PyCharm

'''
题目：输入一个字符串s，输出将该字符串中所有的单词反转顺序后的字符串，单词之间用空格隔开，要求反转前后字符串s的长度相同。
例如：输入" I am a  student. "，输出为" I ma a  .tneduts "。
'''

class Solution:
    def reverseWordsInString(self, s):
        if not s or len(s) <= 0:
            return s
        s1 = s.split(" ")
        for i in range(len(s1)):
            s1[i] = s1[i][::-1]
        res = ' '.join(s1)
        return res

if __name__ == "__main__":
    a = Solution()
    s = " I am a  student. "
    res = a.reverseWordsInString(s)
    print(res)