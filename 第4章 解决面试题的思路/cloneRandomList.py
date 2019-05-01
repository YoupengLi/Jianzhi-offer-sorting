# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 0021 上午 10:52
# @Author  : Youpeng Li
# @Site    : 
# @File    : cloneRandomList.py
# @Software: PyCharm

'''
题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

思路：1. 根据旧链表创建新链表，不去管随机的那个指针
     2. 根据旧链表中的随机指针，创建新链表中的随机指针
     3. 从旧链表中拆分得到新链表
'''

class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution:
    def cloneRandomList(self, pHead: 'RandomListNode') -> 'RandomListNode':
        '''
        返回RandomListNode旧链表
        '''
        if pHead == None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)

    def CloneNodes(self, pHead: 'RandomListNode') -> 'RandomListNode':
        '''
        复制原始链表的每个节点, 将复制的节点链接在其原始节点的后面
        '''
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.val = pNode.val
            pCloned.next = pNode.next

            pNode.next = pCloned
            pNode = pCloned.next

    def ConnectRandomNodes(self, pHead: 'RandomListNode') -> 'RandomListNode':
        '''
        将复制后的链表中的克隆节点的random指针链接到被克隆节点random指针的后一个节点
        '''
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random != None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    def ReconnectNodes(self, pHead: 'RandomListNode') -> 'RandomListNode':
        '''
        拆分链表：将原始链表的节点组成新的链表, 复制节点组成复制后的链表
        '''
        pNode = pHead
        pClonedHead = pClonedNode = pNode.next
        pNode.next = pClonedNode.next
        pNode = pNode.next
        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        return pClonedHead

if __name__ == "__main__":
    '''
           —————————
          |         |
          V         |
     A -> B -> C -> D -> E
     |____|____^         ^
          |______________|
    
    '''
    p1 = RandomListNode('A')
    p2 = RandomListNode('B')
    p3 = RandomListNode('C')
    p4 = RandomListNode('D')
    p5 = RandomListNode('E')

    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5

    p1.random = p3
    p2.random = p5
    p4.random = p2

    head = p1

    a = Solution()
    res = a.cloneRandomList(head)
    print(res.val)
