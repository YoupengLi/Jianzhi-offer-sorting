# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 0014 上午 8:22
# @Author  : Youpeng Li
# @Site    : 
# @File    : fibonacci.py
# @Software: PyCharm

'''
题目：输入一个整数n，输出斐波那契数列的第n项。

       | 0, (n=0)
f(n) = | 1, (n=1)
       | f(n-1)+f(n-2) ,(n>=2,n为整数)
'''

class Solution:
    def fibonacci(self, n: 'int') -> 'int':
        res = [0, 1]
        while len(res) <= n:
            res.append(res[-1]+res[-2])
        return res[n]

if __name__ == "__main__":
    a = Solution()
    n = 39
    print(a.fibonacci(n))