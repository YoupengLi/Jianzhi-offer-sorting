# -*- coding: utf-8 -*-
# @Time    : 2019/1/26 0026 下午 8:14
# @Author  : Youpeng Li
# @Site    : 
# @File    : getNumberOfK.py
# @Software: PyCharm

'''
题目：统计一个数字在排序数组中出现的次数。
例如输入排序数组{1,2,3,3,3,3,4,5}和数字3，由于3在这个数组中出现了4次，因此输出4。

思路：利用二分查找算法，确定重复出现的数字k的第一个和最后一个位置。
查找第一个k：  中间数字>k   k出现在前半段
             中间数字<k   k出现在后半段
             中间数字=k   看中间数字的前面一个数字是不是k，若不是，则为第一个k；若是，k出现在前半段

查找最后一个k： 中间数字>k   k出现在前半段
             中间数字<k   k出现在后半段
             中间数字=k   看中间数字的后面一个数字是不是k，若不是，则为最后一个k；若是，k出现在后半段

'''

class Solution:
    def getNumberOfK(self, arr: 'list[int]', k: 'int') -> 'int':
        if not arr or len(arr) <= 0:
            return 0
        num = 0
        length = len(arr)
        First = self.getFirst(arr, k, 0, length - 1)
        Last = self.getLast(arr, k, 0, length - 1)
        if First > -1:
            num = Last - First + 1
        return num

    def getFirst(self, arr: 'list[int]', k: 'int', start: 'int', end: 'int') -> 'int':
        if start > end:
            return -1
        mid = (start + end) // 2
        if arr[mid] == k:
            if mid > 0 and arr[mid - 1] == k:
                end = mid - 1
            else:
                return mid
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
        return self.getFirst(arr, k, start, end)

    def getLast(self, arr: 'list[int]', k: 'int', start: 'int', end: 'int') -> 'int':
        if start > end:
            return -1
        mid = (start + end) // 2
        if arr[mid] == k:
            if mid < end and arr[mid + 1] == k:
                start = mid + 1
            else:
                return mid
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
        return self.getLast(arr, k, start, end)

if __name__ == "__main__":
    a = Solution()
    arr = [1, 2, 3, 3, 3, 3, 4, 5, 5]
    res = a.getNumberOfK(arr, 5)
    print(res)
    arr = [3]
    res = a.getNumberOfK(arr, 4)
    print(res)