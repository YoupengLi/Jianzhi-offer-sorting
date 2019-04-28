# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 0014 上午 8:53
# @Author  : Youpeng Li
# @Site    : 
# @File    : rectCover.py
# @Software: PyCharm

'''
题目：假设我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

依旧是斐波那契数列，2*n的大矩形和n个2*1的小矩形，其中 2*target 为大矩阵的大小
有以下几种情形：
a. target = 0 大矩形为2*0，直接return 1；
b. target = 1 大矩形为2*1，只有一种摆放方法，return 1；
c. target = 2 大矩形为2*2，有两种摆放方法，return 2；
d. target = n 分为两步考虑：
第一次摆放一块 2*1 的小矩阵，则摆放方法总共为f(target - 1)
√
√
第一次摆放一块1*2的小矩阵，则摆放方法总共为f(target - 2)
√	√
×	×
target >= 3  f(n) = f(target - 1) + f(targte - 2)
'''

class Solution:
    def rectCover(self, num: 'int') -> 'int':
        res = [0, 1, 2]
        while len(res) <= num:
            res.append(res[-1] + res[-2])
        return res[num]

if __name__ == "__main__":
    a = Solution()
    num = 3
    print(a.rectCover(num))