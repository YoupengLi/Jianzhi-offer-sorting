# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 上午 8:32
# @Author  : Youpeng Li
# @Site    : 
# @File    : twoQueueForOneStack.py
# @Software: PyCharm

'''
题目：用两个队列来实现一个栈，完成栈的Push和Pop操作。 栈中的元素为int类型。

有两个队列queueA、queueB，A是入队列的，B是出队列的，入队列时，直接进入A即可。
出队列时，先判断A中是否只有一个元素。
如果A中只有一个元素，直接pop出即可，
如果A中有多于一个元素，不断将A中的元素压入B中，直至只剩最后一个元素，将该元素pop出来，最后将B中所有元素压入A中。
'''

class Solution:
    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, node: 'int') -> 'list[int]':
        self.queueA.insert(0, node)

    def pop(self) -> 'int':
        if not self.queueA:
            return None
        while len(self.queueA) != 1:
            self.queueB.insert(0, self.queueA.pop())
        self.queueA, self.queueB = self.queueB, self.queueA
        return self.queueB.pop()

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