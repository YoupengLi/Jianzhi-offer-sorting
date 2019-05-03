# -*- coding: utf-8 -*-
# @Time    : 2019/2/8 0008 下午 9:05
# @Author  : Youpeng Li
# @Site    : 
# @File    : isContinuous.py
# @Software: PyCharm

'''
题目：LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,
黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,
并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何。为了方便起见,
你可以认为大小王是0。

思路：将这5张牌看成是由5个数字组成的数组，大小王是特殊的数字，不妨把它们都定义为0。
<1> 首先把数组排序；
<2> 再统计数组中0的个数；
<3> 最后统计排序后的数组中相邻数字之间的空缺总数。如果空缺总数小于或者等于0的个数，那么这个数组是连续的，反之则不连续。
注意：如果数组中的非零数字重复出现，则该数组不是连续的。
'''

class Solution:
    def isContinuous(self, nums: 'list[int]') -> 'bool':
        if not nums or len(nums) != 5:
            return False
        nums.sort()
        zero = nums.count(0)

        # 里面有nums[i+1]操作，所以取不到最后一个数
        for i, v in enumerate(nums[:-1]):
            if v != 0:
                # nums中不能有两个相同的数字
                if nums[i + 1] == v:
                    return False
                zero = zero - (nums[i + 1] - v - 1)
                if zero < 0:
                    return False
        return True

if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 5, 0, 0]
    print(a.isContinuous(nums))
    nums = [1, 2, 5, 5, 0]
    print(a.isContinuous(nums))