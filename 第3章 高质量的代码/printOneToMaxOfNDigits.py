# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 0016 下午 4:48
# @Author  : Youpeng Li
# @Site    : 
# @File    : printOneToMaxOfNDigits.py
# @Software: PyCharm

'''
题目：输入数字n,按顺序打印出从1到最大的n位十进制数，比如输入3，则打印出1、2、3一直到最大的3位数999。

解题思路：需要考虑大数问题，这是题目设置的陷阱。可以把问题转换成数字排列问题，用递归让代码更简洁。
'''

class Solution:
    def printOneToMaxOfNDigits(self, n: 'int'):
        if n <= 0:
            return
        num = ['0']*n
        for i in range(10):
            num[0] = str(i)
            self.printOneToMaxOfNDigitsRecursively(num, n, 0)

    def printNumber(self, num: 'int'):
        #此处的number为一个str类型的数组，每个数组元素是一个0-9之间数字的字符串形式
        isBeginning0 = True
        nLength = len(num)
        for i in range(nLength):
            if isBeginning0 and num[i] != '0':
                isBeginning0 = False
            if not isBeginning0:
                print('%c' % num[i], end="")
        # 为了解决第一次循环后不输出0但会输出空行的问题
        if not isBeginning0:
            print('\t')

    def printOneToMaxOfNDigitsRecursively(self, num: 'int', length: 'int', index: 'int'):
        if index == length-1:
            self.printNumber(num)
            return
        for i in range(10):
            num[index+1] = str(i)
            self.printOneToMaxOfNDigitsRecursively(num, length, index+1)

if __name__ == "__main__":
    a = Solution()
    a.printOneToMaxOfNDigits(2)