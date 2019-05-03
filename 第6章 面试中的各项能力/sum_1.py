# -*- coding: utf-8 -*-
# @Time    : 2019/2/9 0009 上午 8:34
# @Author  : Youpeng Li
# @Site    : 
# @File    : sum_1.py
# @Software: PyCharm

'''
题目：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

class Solution:
    '''
    解法一：利用虚函数求解。
    利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况，如果对n连续进行两次反运算，
    那么非零的n转换为True，0转换为False。利用这一特性终止递归。注意考虑测试用例为0的情况。
    '''
    def sum_1(self, n: 'int') -> 'int':
        return self.sum(n)

    def sum0(self, n: 'int') -> 'int':
        return 0

    def sum(self, n: 'int') -> 'int':
        func = {False: self.sum0, True: self.sum}
        return n + func[not not n](n - 1)

    '''
    解法二：终止递归采用逻辑与的短路特性
    '''
    def sum_2(self, n: 'int') -> 'int':
        return n and n + self.sum_2(n-1)

if __name__ == "__main__":
    a = Solution()
    print(a.sum_1(5))
    print(a.sum_2(5))