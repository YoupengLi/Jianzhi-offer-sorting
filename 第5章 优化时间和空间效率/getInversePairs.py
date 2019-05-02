# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 0024 下午 10:47
# @Author  : Youpeng Li
# @Site    : 
# @File    : getInversePairs.py
# @Software: PyCharm

'''
题目：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组
中的逆序对的总数P。
eg:
在数组{7, 5, 4, 6}中，一共存在5个逆序对，分别是(7,6)、(7,5)、(7,4)、(6,4)、(5,4)。

归并排序法：
7 5 6 4
<1> 把长度为4的数组分解成两个长度为2的子数组
7 5 和 6 4
<2> 把长度为2的数组分解成两个长度为1的子数组
7 和 5   和  6 和 4
<3> 把长度为1的子数组合并、排序，并统计逆序对
5 7 （1） 和 4 6 （1）
<4> 把长度为2的子数组合并、排序，并统计逆序对
7 和 6 4 （2） 5 和 4 （1）

合并两个子数组 5 7 和 4 6 并统计逆序对的过程：
p1指向前半段最后一个数字7，p2指向后半段最后一个数字6，p3指向辅助数组的最后一位。
由于p1指向的数字大于p2指向的数字，表明数组中存在逆序对。把逆序对数目加2，并把p1指向的数7复制到辅助数组，向前移动p1和p3。
p1向前移动一位，由于p1指向的数字小于p2指向的数字，表明数组中没有逆序对。把p2指向的数6复制到辅助数组，向前移动p2和p3。
由于p1指向的数字大于p2指向的数字，表明数组中存在逆序对。把逆序对数目加1，把p1指向的数5复制到辅助数组，向前移动p1和p3。
剩下前半段数组还剩一个4，将其复制到辅助数组中。
'''

import time
import numpy as np

class Solution:
    '''
    方法一：巧妙的方法，来源牛客网
    找到最小元素，索引值即为与之相关的逆序对数；
    剔除该最小元素，继续上述操作，直到只有一个元素
    '''
    def getInversePairs(self, arr: 'list[int]'):
        start_time = time.clock()
        if arr == []:
            end_time = time.clock()
            return 0, end_time - start_time
        else:
            count = 0
            while len(arr) > 1:
                count += arr.index(min(arr))
                arr.pop(arr.index(min(arr)))
            end_time = time.clock()
            return count, end_time - start_time

    '''
    方法二：对方法一的改进
    先排序，就不用每次去找最小值了，以空间换时间
    '''
    def getInversePairs_1(self, arr: 'list[int]'):
        start_time = time.clock()
        if len(arr) <= 0:
            end_time = time.clock()
            return 0, end_time - start_time
        count = 0
        copy = arr[:]
        copy.sort()
        for i in range(0, len(arr)-1):
            count += arr.index(copy[i])
            arr.remove(copy[i])
        end_time = time.clock()
        return count, end_time - start_time

    '''
    方法三：归并排序法
    '''
    def getInversePairs_2(self, arr: 'list[int]'):
        start_time = time.clock()
        if len(arr) <= 0:
            end_time = time.clock()
            return 0, end_time - start_time
        length = len(arr)
        # copy数组为原数组data的复制,在后面充当辅助数组
        copy = arr[:]
        count = self.Core(arr, copy, 0, length - 1)
        end_time = time.clock()
        return count, end_time - start_time

    def Core(self, arr: 'list[int]', copy: 'list[int]', start: 'int', end: 'int') -> 'int':
        if start == end:
            copy[start] = arr[start]
            return 0

        length = (end - start) // 2  # length为划分后子数组的长度

        left = self.Core(copy, arr, start, start + length)
        right = self.Core(copy, arr, start + length + 1, end)

        # 初始化i为前半段最后一个数字的下标
        i = start + length
        # 初始化j为后半段最后一个数字的下标
        j = end

        # indexCopy为辅助数组的指针，初始化其指向最后一位
        indexCopy = end
        # 准备开始计数
        count = 0
        # 对两个数组进行对比取值的操作：
        while i >= start and j >= start + length + 1:
            if arr[i] > arr[j]:
                copy[indexCopy] = arr[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = arr[j]
                indexCopy -= 1
                j -= 1

        # 剩下一个数组未取完的操作：
        while i >= start:
            copy[indexCopy] = arr[i]
            indexCopy -= 1
            i -= 1
        while j >= start + length + 1:
            copy[indexCopy] = arr[j]
            indexCopy -= 1
            j -= 1

        return count + left + right

if __name__ == "__main__":
    a = Solution()
    arr = np.arange(1, 10000)
    arr = np.append(arr, 0)
    arr = arr.tolist()
    print(a.getInversePairs(arr))
    arr = np.arange(1, 80000)
    arr = np.append(arr, 0)
    arr = arr.tolist()
    print(a.getInversePairs_1(arr))
    arr = np.arange(1, 80000)
    arr = np.append(arr, 0)
    arr = arr.tolist()
    print(a.getInversePairs_2(arr))