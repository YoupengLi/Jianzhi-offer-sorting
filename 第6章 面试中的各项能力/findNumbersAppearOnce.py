# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 0027 上午 9:06
# @Author  : Youpeng Li
# @Site    : 
# @File    : findNumbersAppearOnce.py
# @Software: PyCharm

'''
题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
要求时间复杂度为o(n)，空间复杂度为o(1)。
eg:
输入：{2,4,3,6,3,2,5,5}
输出：[4,6]

异或运算的性质：任何一个数字异或它自己都等于0。
解题思路：从头到尾依次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果。
然后找到最右边为1的位的位置（只出现一次的两个数字在该位必然不同），
以第n位是不是1为标准将原数组的数字分成两个字数组，则每个字数组均包含一个只出现一次的数字。
'''

class Solution:
    # 返回[a,b] 其中a、b是出现一次的两个数字
    def findNumbersAppearOnce(self, arr: 'list[int]') -> [int, int]:
        if len(arr) < 2:
            return
        resultEOR = 0
        for i in arr:
            resultEOR = resultEOR ^ i

        index = self.findFirstBit(resultEOR)

        res1, res2 = 0, 0
        for i in arr:
            if self.isBit(i, index):
                res1 ^= i
            else:
                res2 ^= i
        return [res1, res2]

    def findFirstBit(self, num: 'int') -> 'int':
        '''
        用于在整数num的二进制表示中找到最右边是1的位
        '''
        indexBit = 0
        while (num & 1 == 0 and indexBit < 32):
            num = num >> 1
            indexBit += 1
        return indexBit

    def isBit(self, num: 'int', indexBit: 'int'):
        '''
        用于判断在num的二进制表示中从右边起的indexBit位是否为1
        '''
        num = num >> indexBit
        return (num & 1)

if __name__ == "__main__":
    arr = [1, 1, 2, 2, -3, 4, 4, 5]
    a = Solution()
    res = a.findNumbersAppearOnce(arr)
    print(res)