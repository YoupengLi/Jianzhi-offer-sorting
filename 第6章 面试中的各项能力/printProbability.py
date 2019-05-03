# -*- coding: utf-8 -*-
# @Time    : 2019/2/7 0007 上午 8:31
# @Author  : Youpeng Li
# @Site    : 
# @File    : printProbability.py
# @Software: PyCharm

'''
题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n,打印出s的所有可能的值出现的概率。

解题思路：动态规划思想
假设f(m,n)表示投第m个骰子时，点数之和n出现的次数，投第m个骰子的点数之和只与投第m-1个骰子时有关。
递归方程：f(m,n)=f(m-1,n-1)+f(m-1,n-2)+f(m-1,n-3)+f(m-1,n-4)+f(m-1,n-5)+f(m-1,n-6)
表示本轮点数和为n出现的次数等于上一轮点数和为n-1,n-2,n-3,n-4,n-5,n-6出现的次数之和。
'''

class Solution:
    def printProbability(self, n: 'int') -> 'list[float]':
        dp = [[0 for _ in range(6 * n)] for _ in range(n)]

        for i in range(6):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(i, 6 * (i + 1)):  # [0,i-1]的时候，频数为0（例如2个骰子不可能投出点数和为1）
                dp[i][j] = dp[i - 1][j - 6] + dp[i - 1][j - 5] + dp[i - 1][j - 4] + \
                           dp[i - 1][j - 3] + dp[i - 1][j - 2] + dp[i - 1][j - 1]

        count = dp[n - 1]
        count_sum = sum(count)
        count = [i/count_sum for i in count]
        return count  # 骰子投出每一个点数的频数再除以总的排列数即可得到频率

if __name__ == "__main__":
    a = Solution()
    res = a.printProbability(3)  # 括号中的数字为骰子的个数
    [print("投出点数为"+str(i+1)+"的概率: ", res[i]) for i in range(len(res))]