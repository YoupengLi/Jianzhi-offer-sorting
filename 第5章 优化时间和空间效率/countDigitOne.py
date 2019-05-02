# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 0023 上午 10:25
# @Author  : Youpeng Li
# @Site    : 
# @File    : countDigitOne.py
# @Software: PyCharm

'''
从1到n整数中1出现的次数
题目：输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。
例如输入12，从1到12这些整数中包含1的数字有1，10，11和12，1一共出现了5次。

题目：求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、
10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出
任意非负整数区间中1出现的次数。

eg: 21345
<1> 1346~21345
1出现在万位：10000~19999 共10000次
1出现在除万位的其余四位：4000*2=8000
1346~11345：  选择其中一位为1，排列组合共有4*10^3=4000次
11346~21345： 选择其中一位为1，排列组合共有4*10^3=4000次

<2> 346~1345
1出现在千位：1000~1345 共345+1=346次
1出现在除千位的其余三位：300*1=300
346~1345： 选择其中一位为1，排列组合共有3*10^2=300次

<3> 46~345
1出现在百位：100~199 共100次
1出现在除百位的其余两位：20*3=60
46~145：  选择其中一位为1，排列组合共有2*10^1=20次
146~245： 选择其中一位为1，排列组合共有2*10^1=20次
246~345： 选择其中一位为1，排列组合共有2*10^1=20次

<4> 6~45
1出现在十位：10~19 共10次
1出现在除十位的其余一位：1*4=4
6~15：  选择其中一位为1，排列组合共有1*10^0=1次
16~25： 选择其中一位为1，排列组合共有1*10^0=1次
26~35： 选择其中一位为1，排列组合共有1*10^0=1次
36~45： 选择其中一位为1，排列组合共有1*10^0=1次

<5> 1~5 共1次
'''

class Solution:
    def countDigitOne(self, n: 'int') -> 'int':
        res = 0
        if n < 0:
            return 0
        length = len(str(n))
        listN = list(str(n))

        for i, v in enumerate(listN):
            a = length - i - 1  # a为10的幂
            if i == length - 1 and int(v) >= 1:
                res += 1
                break
            if int(v) > 1:
                res += int(a * 10 ** (a-1)) * int(v) + 10 ** a
            if int(v) == 1:
                res += (int(a * 10 ** (a-1)) + int("".join(listN[i + 1:])) + 1)
        return res

if __name__ == "__main__":
    a = Solution()
    print(a.countDigitOne(21345))
