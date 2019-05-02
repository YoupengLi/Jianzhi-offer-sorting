# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 0022 下午 7:34
# @Author  : Youpeng Li
# @Site    : 
# @File    : getLeastKNumbers.py
# @Software: PyCharm

'''
题目：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

思路: 这一题应用堆排序算法复杂度只有O(nlog k)，堆是完全二叉树的一种，最大堆就是最上面的数是最大的
该方法基于二叉树或者堆来实现，首先把数组前k个数字构建一个最大堆，然后从第k+1个数字开始遍历数组，如果遍历到的
元素小于堆顶的数字，那么就交换两个数字，重新构造堆，继续遍历，最后剩下的堆就是最小的k个数，时间复杂度O(nlog k)。
'''

class Solution:
    def getLeastKNumbers(self, arr, k):
        import heapq
        if not arr or len(arr) <= 0 or k <= 0 or len(arr) < k:
            return []

        # 建立最小堆，最上面那个数是最小的，返回一个列表，这个列表就是从最小值开始的k个数
        return heapq.nsmallest(k, arr)


if __name__ == "__main__":
    a = Solution()
    arr = [4, 5, 1, 6, 2, 7, 3, 8]
    print(a.getLeastKNumbers(arr, 4))