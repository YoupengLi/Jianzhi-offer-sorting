# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 0019 下午 3:37
# @Author  : Youpeng Li
# @Site    : 
# @File    : StackIncludeMinFunction.py
# @Software: PyCharm

'''
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。

思路：
可以设计两个栈：Stack和StackMin，一个就是普通的栈，另外一个存储push进来的最小值。

首先是push操作：
每次压入的数据newNum都push进Stack中，然后判断StackMin是否为空。
如果为空那也把newNum同步压入StackMin里；
如果不为空，就先比较newNum和StackMin中栈顶元素的大小，
如果newNum较大，那就不压入StackMin里，只压入一个最小值，否则就同步压入StackMin里。

然后是pop操作：同步弹出。
'''

class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node: 'int'):
        self.stack.append(node)
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            self.minstack.append(self.min())

    def pop(self):
        if self.minstack == [] or self.stack == []:
            return None
        self.minstack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minstack[-1]

if __name__ == "__main__":
    a = Solution()
    a.push(3)
    a.push(4)
    a.push(2)
    print(a.min())
    a.push(1)
    print(a.min())
    a.pop()
    a.pop()
    print(a.min())