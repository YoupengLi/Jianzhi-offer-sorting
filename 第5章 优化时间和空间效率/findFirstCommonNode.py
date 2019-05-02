# -*- coding: utf-8 -*-
# @Time    : 2019/1/26 0026 上午 11:17
# @Author  : Youpeng Li
# @Site    : 
# @File    : findFirstCommonNode.py
# @Software: PyCharm
'''
题目：输入两个链表，找出它们的第一个公共结点。

思路：共同节点，意味着从共同节点开始之后所有的节点数都是相同的，这是链表，只要有一个共同节点，那么之后所有的指向
也是重复的。先依次遍历两个链表，记录两个链表的长度m和n，如果 m > n，那么我们就先让长度为m的链表走m-n个结点，然后
两个链表同时遍历，当遍历到相同的结点的时候停止即可。对于 m < n，同理。
'''

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def list_2_listnode(arr: 'list[int]') -> 'ListNode':
    if not arr or len(arr) <= 0:
        return ListNode()
    tem_node = ListNode()
    node = ListNode()
    for i in arr:
        #记得是判定val是否有值，并且用一个node记住头节点，然后返回的是头节点
        if not tem_node.val:
            tem_node.val = i
            node = tem_node
        else:
            tem_node.next = ListNode(i)
            tem_node = tem_node.next
    return node

class Solution:
    def findFirstCommonNode(self, pHead1: 'ListNode', pHead2: 'ListNode') -> 'ListNode':
        length1 = self.GetLength(pHead1)
        length2 = self.GetLength(pHead2)
        if length1 <= 0 or length2 <= 0:
            return None

        if length1 > length2:
            headLong = pHead1
            headShort = pHead2
        else:
            headLong = pHead2
            headShort = pHead1
        diff = abs(length1 - length2)

        for i in range(diff):
            headLong = headLong.next

        while headLong.next != None and headShort.next != None and headLong.val != headShort.val:
            headLong = headLong.next
            headShort = headShort.next
        if headLong.next == None and headLong.val != headShort.val:
            return None
        return headLong

    def GetLength(self, pHead: 'ListNode') -> 'int':
        length = 0
        while pHead:
            pHead = pHead.next
            length += 1
        return length

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    l1 = list_2_listnode(arr1)
    arr2 = [6, 8, 10, 2, 3, 4, 5]
    l2 = list_2_listnode(arr2)
    a = Solution()
    res = a.findFirstCommonNode(l1, l2)
    print(res.val)