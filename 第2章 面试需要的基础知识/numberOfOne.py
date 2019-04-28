# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 0015 上午 8:24
# @Author  : Youpeng Li
# @Site    : 
# @File    : numberOfOne.py
# @Software: PyCharm
'''
题目：请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。
例如把9表示成二进制为 1001，有2位是，因此如果输入9，该函数输出2；
把-7表示成二进制为 11111111111111111111111111111001，有30位是1，
因此如果输入-7，该函数输出30。
class Solution:
    def numberOfOne(self, n: 'int') -> 'int':
        return bin(n & 0xffffffff).count("1")
'''

class Solution:
    def numberOfOne(self, n: 'int') -> 'int':
        count = 0
        # 获取负数的补码形式的二进制表示
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = (n-1) & n
            count += 1
        return count

if __name__ == "__main__":
    a = Solution()
    print(a.numberOfOne(-7))
    print(a.numberOfOne(64))