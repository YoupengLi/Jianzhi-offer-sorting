# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 上午 10:42
# @Author  : Youpeng Li
# @Site    : 
# @File    : findKthToTail.py
# @Software: PyCharm

'''
题目：链表中倒数第k个节点。输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如链表有6个节点，从头节点开始它们的值依次是1、2、3、4、5、6。
这个链表的倒数第3个节点是值为4的节点。

'''

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def findKthToTail(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if not head or k <= 0:
            return None
        pAhead = head
        for i in range(k-1):
            if pAhead.next:
                pAhead = pAhead.next
            else:
                return None
        pBehind = head
        while pAhead.next:
            pAhead = pAhead.next
            pBehind = pBehind.next
        return pBehind

if __name__ == "__main__":
    '''
    A -> B -> C -> D -> E -> F -> G -> H
    '''
    t1 = ListNode('A')
    t2 = ListNode('B')
    t3 = ListNode('C')
    t4 = ListNode('D')
    t5 = ListNode('E')
    t6 = ListNode('F')
    t7 = ListNode('G')
    t8 = ListNode('H')

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t6
    t6.next = t7
    t7.next = t8

    head = t1

    a = Solution()
    print(a.findKthToTail(head, 1))
    print(a.findKthToTail(head, 9))