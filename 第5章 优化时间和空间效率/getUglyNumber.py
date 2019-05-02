# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 0024 上午 10:19
# @Author  : Youpeng Li
# @Site    : 
# @File    : getUglyNumber.py
# @Software: PyCharm

'''
题目：把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

思路：按顺序把每个丑数放在数组中，求下一个丑数
下一个丑数必定由有数组中的某一个丑数A * 2， B * 3， C * 5 的中的最小值得来。
在数组中必定有一个丑数M2， 在它之前的数 * 2 都小于当前最大丑数， 在它之后的数 * 2都大于当前最大丑数，
同样有M3, M5。
'''

class Solution:
    def getUglyNumber(self, index: 'int') -> 'int':
        if index < 1:
            return 0
        res = [1]
        t2 = t3 = t5 = 0
        nextind = 1
        while nextind < index:
            minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            res.append(minNum)
            while res[t2] * 2 <= minNum:
                t2 += 1
            while res[t3] * 3 <= minNum:
                t3 += 1
            while res[t5] * 5 <= minNum:
                t5 += 1
            nextind += 1
        return res[nextind - 1]

if __name__ == "__main__":
    a = Solution()
    print(a.getUglyNumber(1500))