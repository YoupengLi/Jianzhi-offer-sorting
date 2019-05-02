# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 0022 下午 4:15
# @Author  : Youpeng Li
# @Site    : 
# @File    : moreThanHalfNumber.py
# @Software: PyCharm

'''
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

思路1：快排，如果该数出现次数超过数组长度的一半，那么，排序之后，他应该位于数组的中间
思路2：根据数组的特点，出现次数超过一半的数，他出现的次数比其他数字出现的总和还要多，因此可以最开始保存两个数值：
数组中的一个数字以及它出现的次数，然后遍历，如果下一个数字等于这个数字，那么次数加一，如果不等，次数减一，当次数
等于0的时候，在下一个数字的时候重新复制新的数字以及出现的次数置为1，直到进行到最后，然后再验证最后留下的数字是否
出现次数超过一半，因为可能前面的次数依次抵消掉，最后一个数字就直接是保留下来的数字，但是出现次数不一定超过一半。
'''

class Solution:
    def moreThanHalfNumber(self, arr: 'list[int]') -> 'int':
        if not arr or len(arr) <= 0:
            return 0
        arr.sort()
        res = arr[(len(arr)+1)//2]

        sum = 0
        for i in arr:
            if i == res:
                sum += 1
        return res if sum * 2 > len(arr) else 0


    def moreThanHalfNumber_1(self, arr: 'list[int]') -> 'int':
        if not arr or len(arr) <= 0:
            return 0

        # 若存在则该数出现次数比其他所有数字出现次数之和还要多，
        # 则要找的数字肯定是最后一次把次数设为1时对应的数字
        res = arr[0]
        times = 1
        for i in range(1, len(arr)):
            if times == 0:
                res = arr[i]
                times = 1
            elif arr[i] == res:
                times += 1
            else:
                times -= 1

        sum = 0
        for i in arr:
            if i == res:
                sum += 1
        return res if sum * 2 > len(arr) else 0

if __name__ == "__main__":
    a = Solution()
    arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    res = a.moreThanHalfNumber(arr)
    print(res)
    arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    res = a.moreThanHalfNumber_1(arr)
    print(res)