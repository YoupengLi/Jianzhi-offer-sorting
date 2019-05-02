# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 0022 下午 9:25
# @Author  : Youpeng Li
# @Site    : 
# @File    : findGreatestSumOfSubarray.py
# @Software: PyCharm

'''
连续数组的最大和
题目：输入一个整型数组，数组里有正数也有负数。数组中一个或者连续的多个整数组成一个子数组。求所有子数组和的最大值。
要求时间复杂度为o(n)。

题目：HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常
需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望
旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。你会不会被他
忽悠住？(子向量的长度至少是1)

'''


class Solution:
    '''
    法一：
    对于连续子数组，可以用一个数值来存储当前和，如果当前和小于零，那么在进行到下一个元素的时候，直接把当前和赋值为下一个元素，
    如果当前和大于零，则累加下一个元素，同时用一个maxNum存储最大值并随时更新。
    '''
    def findGreatestSumOfSubarray(self, arr: 'list[int]') -> 'int':
        if not arr or len(arr) <= 0:
            return 0

        maxNum = 0
        res = arr[0]
        for i in range(len(arr)):
            if maxNum <= 0:
                maxNum = arr[i]
            else:
                maxNum += arr[i]
            if maxNum > res:
                res = maxNum
        return res

    '''
    法二：动态规划
    用函数f(i)来表示以第i个数字结尾的子数组的最大和
    f(i) =  | arr[i],           i=0 or f(i-1)<=0
            | f(i-1)+arr[i],    i>0 and f(i-1)>0
    '''
    def findGreatestSumOfSubarray_1(self, arr: 'list[int]') -> 'int':
        if not arr or len(arr) <= 0:
            return 0

        res = [0] * len(arr)
        res[0] = arr[0]
        for i in range(1, len(arr)):
            if res[i-1] <= 0:
                res[i] = arr[i]
            else:
                res[i] = res[i-1] + arr[i]
        return max(res)

if __name__ == "__main__":
    a = Solution()
    arr = [6, -3, -2, 7, -15, 1, 2, 2]
    res = a.findGreatestSumOfSubarray(arr)
    print(res)
    res = a.findGreatestSumOfSubarray_1(arr)
    print(res)

