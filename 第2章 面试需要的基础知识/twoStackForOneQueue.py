# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 上午 8:31
# @Author  : Youpeng Li
# @Site    : 
# @File    : twoStackForOneQueue.py
# @Software: PyCharm

'''
题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

有两个栈stackA、stackB，A是入栈的，B是出栈的，入栈时，直接进入A即可。
出栈时，先判断是否有元素。
如果B没有元素，pop肯定报错，应该先将A中所有的元素压入B中，再pop最上面一个元素，
如果B中有就直接pop出，就可以。
'''

class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node: 'int') -> 'list[int]':
        self.stackA.append(node)

    def pop(self) -> 'int':
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()

if __name__== "__main__":
    a=Solution()
    a.push(1)
    a.push(7)
    a.push(3)
    a.push(5)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())