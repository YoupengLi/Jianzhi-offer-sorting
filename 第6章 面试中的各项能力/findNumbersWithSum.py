# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 0027 下午 8:55
# @Author  : Youpeng Li
# @Site    : 
# @File    : findNumbersWithSum.py
# @Software: PyCharm

'''
题目：输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出任意一对即可。

思路：设定两个指针，一个指向数组的起点，一个指向数组的终点，然后对两个数字求和，如果和大于目标值，则把后一个指针前移，
如果和小于目标值，则把前一个指针后移。两个指针交汇的时候如果还没找到，就终止操作。
'''
class Solution:
    def findNumbersWithSum(self, arr: 'list[int]', tsum: 'int') -> '[int, int]':
        if not arr or len(arr) <= 0 or arr[-1] + arr[-2] < tsum:
            return []
        start = 0
        end = len(arr) - 1
        while start < end:
            if arr[start] + arr[end] < tsum:
                start += 1
            elif arr[start] + arr[end] > tsum:
                end -= 1
            else:
                return [arr[start], arr[end]]
        return []

if __name__ == "__main__":
    a = Solution()
    arr = [1, 2, 4, 7, 11, 15]
    res = a.findNumbersWithSum(arr, 15)
    print(res)