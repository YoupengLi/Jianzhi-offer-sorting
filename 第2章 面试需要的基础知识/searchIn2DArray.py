# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 0010 上午 10:41
# @Author  : Youpeng Li
# @Site    :
# @File    : searchIn2DArray.py
# @Software: PyCharm

'''
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


方法一： 循环迭代查找，不是最优
class Solution:
    def searchIn2DArray(self, arr: 'list[int]', target: 'int') -> 'bool':
        # write code here
        if not arr or len(arr) <= 0 or not len(arr[0]) or len(arr[0]) <= 0:
            return
        row = len(arr)
        col = len(arr[0])
        for i in range(row):
            for j in range(col):
                if arr[i][j] == target:
                    return True
        return False

方法二：上述方法的时间复杂度是O(n^2)，最优化的方式是从右上或者左下开始搜索
从右上开始搜索，如果数组中的数比该数要大，那么想左移动一位；如果数组中的数比该数小，向下移动一位
因为数组本身是从左到右依次增大，从上到下依次增大
'''


class Solution:
    def searchIn2DArray(self, arr: 'list[int]', target: 'int') -> 'bool':
        # 从右上开始搜索
        if not isinstance(target, int):
            print('Error! The searched objective is not integer.')
            return
        elif not arr or len(arr) <= 0 or not len(arr[0]) or len(arr[0]) <= 0:
            return
        else:
            m, n = len(arr), len(arr[0])
            row = 0
            col = n - 1
            while (row < m and col >= 0):
                if arr[row][col] < target:
                    row += 1
                elif arr[row][col] > target:
                    col -= 1
                else:
                    return True
            return False

    def searchIn2DArray_1(self, arr, target):
        # 从左下开始搜索
        if not isinstance(target, int):
            print('Error! The searched objective is not integer.')
            return
        elif not arr or len(arr) <= 0 or not len(arr[0]) or len(arr[0]) <= 0:
            return
        else:
            m, n = len(arr), len(arr[0])
            row = m - 1
            col = 0
            while (row >= 0 and col < n):
                if arr[row][col] < target:
                    col += 1
                elif arr[row][col] > target:
                    row -= 1
                else:
                    return True
            return False

if __name__ == "__main__":
    a = Solution()
    arr = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    res = a.searchIn2DArray(arr, 7)
    print(res)
    res = a.searchIn2DArray_1(arr, 7)
    print(res)
    res = a.searchIn2DArray(arr, 0)
    print(res)
    res = a.searchIn2DArray_1(arr, 17)
    print(res)
    res = a.searchIn2DArray(arr, None)
    print(res)