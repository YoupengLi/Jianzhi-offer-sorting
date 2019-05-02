# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 0022 上午 9:24
# @Author  : Youpeng Li
# @Site    : 
# @File    : stringPermutation.py
# @Software: PyCharm

'''
题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

依次取一个元素，然后依次和之前递归形成的所有子串组合，形成新的字符串。
'''

class Solution:
    def stringPermutation(self, s):
        if not len(s):
            return []
        if len(s) == 1:
            return list(s)

        charList = list(s)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i-1]:
                continue
            temp = self.stringPermutation(''.join(charList[:i])+''.join(charList[i+1:]))
            for j in temp:
                pStr.append(charList[i]+j)
        return pStr

if __name__ == "__main__":
    a = Solution()
    s = 'abca'
    print(a.stringPermutation(s))