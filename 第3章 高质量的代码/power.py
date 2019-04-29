# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 0015 下午 6:48
# @Author  : Youpeng Li
# @Site    : 
# @File    : power.py
# @Software: PyCharm

'''
题目：
实现函数double Power(double base, int exponent)，求base的exponent次方、不得使用库函数，同时不需要考虑大数问题。

方法一： 利用python函数，直接通过
class Solution:
    def Power(self, base: 'double', exponent: 'int') -> 'double':
        return base**exponent
'''

class Solution:
    '''
    方法二：主题考虑底数为0.0，指数为负数的情况，此时可以利用全局变量指出g_InvalidInput为True,同时返回0.0
    '''
    def __init__(self):
        self.g_InvalidInput = False

    def power(self, base: 'double', exponent: 'int') -> 'double':
        if base == 0.0 and exponent < 0:
            g_InvalidInput = True
            return 0.0
        if exponent >= 0:
            return self.powerWithUnsignedExponent(base, exponent)
        return 1.0 / self.powerWithUnsignedExponent(base, -exponent)

    def powerWithUnsignedExponent(self, base: 'double', exponent: 'int') -> 'double':
        result = 1.0
        for i in range(exponent):
            result *= base
        return result

    '''
    方法三（方法二的优化）：
    上述代码PowerWithUnsignedExponent部分还可以优化如下：
    使用平方的一半*平方的一半来计算平方，此时时间复杂度为O(logn)。
    同时涉及除以2用右移运算符代替，判断奇偶数时用位与运算代替求余运算符，这样效率高很多。
    def __init__(self):
        self.g_InvalidInput = False
    '''
    def power_1(self, base: 'double', exponent: 'int') -> 'double':
        if base == 0.0 and exponent < 0:
            self.g_InvalidInput = True
            return 0.0
        if exponent >= 0:
            return self.powerWithUnsignedExponent_1(base, exponent)
        return 1.0/self.powerWithUnsignedExponent_1(base, -exponent)

    def powerWithUnsignedExponent_1(self, base: 'double', exponent: 'int') -> 'double':
        if exponent == 0:
            return 1.0
        if exponent == 1:
            return base
        res = self.powerWithUnsignedExponent_1(base, exponent >> 1)
        res *= res
        # 判断奇偶数，若为奇数，再乘以base
        if exponent & 0x1 == 1:
            res *= base
        return res

if __name__ == "__main__":
    a = Solution()
    print(a.power(2, 0))
    print(a.power(2, -1))
    print(a.power_1(2, 0))
    print(a.power_1(2, -1))