# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 0016 下午 8:23
# @Author  : Youpeng Li
# @Site    : 
# @File    : deleteNode.py
# @Software: PyCharm

'''
题目：
在O(1)时间内删除链表节点。给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。

解题思路：要删除节点i,先把i的下一个节点j的内容复制到i,然后把i的指针指向节点j的下一个节点。
'''

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, head: 'ListNode', node: 'ListNode') -> 'ListNode':
        """
        删除指定节点
        """
        # 链表只有一个节点，删除头节点
        if head == node:
            del node

        # 链表中有多个节点，删除的节点是尾节点
        elif not node.next:
            temp = head
            while temp.next != node:
                temp = temp.next
            temp.next = None

        # 要删除的节点不是尾节点
        else:
            temp = node.next
            node.val = temp.val
            node.next = temp.next
            del temp

        return head

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
    res = a.deleteNode(head, t2)
    print(res.val)