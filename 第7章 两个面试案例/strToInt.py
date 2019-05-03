# -*- coding: utf-8 -*-
# @Time    : 2019/2/9 0009 下午 10:57
# @Author  : Youpeng Li
# @Site    : 
# @File    : strToInt.py
# @Software: PyCharm

'''
题目：将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

思路：就是一些特殊处理，比如 +123，就不合理，123前面不需要+，但是-123就合理，因为这是个负数。
'''

class Solution:
    def strToInt(self, s: 'str') -> 'int':
        if not s or len(s) <= 0:
            return 0
        num = []
        numbers = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        for i in s:
            if i in numbers.keys():
                num.append(numbers[i])
            elif i == '+':
                continue
            elif i == '-':
                continue
            else:
                return 0
        res = 0
        for i in num:
            res = res * 10 + i
        if s[0] == '-':
            res = 0 - res
        return res

if __name__ == "__main__":
    a = Solution()
    res = a.strToInt('-1230')
    print(res)