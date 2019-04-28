# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 0010 下午 2:22
# @Author  : Youpeng Li
# @Site    : 
# @File    : replaceSpace.py
# @Software: PyCharm

'''
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

方法一：
class Solution:
    # s 源字符串
    def replaceSpace(self, s: 'str') -> 'str':
        # write code here
        return '%20'.join(s.split(' '))

方法二：
class Solution:
    # s 源字符串
    def replaceSpace(self, s: 'str') -> 'str':
        # write code here
        return s.replace(' ','%20')

剑指offer解法：
<1>先计算源字符串数组长度，并统计空格数量
<2>新字符串数组长度=源数组长度+2*空格数量
<3>在新字符串数组上，从后向前遍历，通过两个index移动并复制。
'''

class Solution:
    # s 源字符串
    def replaceSpace(self, s: 'str') -> 'str':
        # method 1:
        # return '%20'.join(s.split(' '))

        # method 2:
        # return s.replace(' ','%20')

        # method 3:
        # 计算空格数量
        if not isinstance(s, str):
            print('Error! The input s is not a string.')
            return
        else:
            s = list(s)
            count = 0
            for e in s:
                if e == ' ':
                    count += 1
            p1 = len(s) - 1  # p1为原始字符串数组末尾的index
            # 求新数组长度
            s += [None] * (count * 2)
            p2 = len(s) - 1  # p2为新字符串数组末尾的index
            while p1 < p2:
                if s[p1] == ' ':
                    for i in ['0', '2', '%']:
                        s[p2] = i
                        p2 -= 1
                else:
                    s[p2] = s[p1]
                    p2 -= 1
                p1 -= 1
            return ''.join(s)

if __name__ == "__main__":
    a = Solution()
    s = "We are happy."
    res = a.replaceSpace(s)
    print(res)
    s = " We are happy."
    res = a.replaceSpace(s)
    print(res)
    s = "We are happy. "
    res = a.replaceSpace(s)
    print(res)
    s4 = "We  are  happy."
    res = a.replaceSpace(s)
    print(res)
    s5 = "Wearehappy."
    res = a.replaceSpace(s)
    print(res)
    s = ""
    res = a.replaceSpace(s)
    print(res)