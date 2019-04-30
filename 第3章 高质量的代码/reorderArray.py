# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 0016 下午 10:48
# @Author  : Youpeng Li
# @Site    : 
# @File    : reorderArray.py
# @Software: PyCharm

'''
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

解题思路：
使用两个指针，第一个指针初始化指向数组的第一个数字，从前向后移动，遇到偶数就停下来；
第二个指针指向数组的最后一个数字，从后向前移动，遇到奇数就停下来，交换两个指针指向的元素，直到两个指针相遇。
'''

class Solution:
    def reorderArray(self, arr: 'list[int]') -> 'list[int]':
        if not arr or len(arr) <= 0:
            return arr
        pBegin = 0
        pEnd = len(arr)-1
        while (pBegin < pEnd):
            while pBegin < pEnd and not self.isEven(arr[pBegin]):
                pBegin += 1
            while pBegin < pEnd and self.isEven(arr[pEnd]):
                pEnd -= 1
            if pBegin < pEnd:
                arr[pBegin], arr[pEnd] = arr[pEnd], arr[pBegin]
        return arr

    def isEven(self, num):
        return num & 1 == 0

    # 不改变奇数与奇数的相对顺序、偶数与偶数的相对顺序
    # 该方法另外开辟存储空间
    def reorderArray_1(self, arr: 'list[int]') -> 'list[int]':
        if not arr or len(arr) <= 0:
            return arr
        odd, even = [], []
        for i in arr:
            odd.append(i) if i % 2 == 1 else even.append(i)
        return odd + even

    # 不改变奇数与奇数的相对顺序、偶数与偶数的相对顺序
    # 不需要另外开辟存储空间
    # 从前往后两两比较，如果前偶后奇，进行交换，然后交换完成后对奇数继续往前判断
    def reorderArray_2(self, arr: 'list[int]') -> 'list[int]':
        if not arr or len(arr) <= 0:
            return arr
        for i in range(len(arr) - 1):
            if arr[i] % 2 == 0 and arr[i + 1] % 2 == 1:  # 前偶数，后奇数就交换
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

            while i > 0:
                if arr[i] % 2 == 1 and arr[i - 1] % 2 == 0:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
        return arr

if __name__ == "__main__":
    a = Solution()
    arr = [1, 2, 3, 4, 5]
    print(a.reorderArray(arr))
    arr = [1, 2, 3, 4, 5]
    print(a.reorderArray_1(arr))
    arr = [1, 2, 3, 4, 5]
    print(a.reorderArray_2(arr))
    arr = [5, 4, 2, 1, -5]
    print(a.reorderArray(arr))
    arr = [5, 4, 2, 1, -5]
    print(a.reorderArray_1(arr))
    arr = [5, 4, 2, 1, -5]
    print(a.reorderArray_2(arr))