# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 0010 下午 3:30
# @Author  : Youpeng Li
# @Site    : 
# @File    : printListFromTailToHead.py
# @Software: PyCharm

'''
题目：输入一个链表，从尾到头打印链表每个节点的值
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
    '''
    方法一：先存入vector，再反转vector
    '''
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, linkNode: 'ListNode') -> 'ListNode':
        if not linkNode:
            return []
        res = []
        while linkNode.next is not None:
            res.append(linkNode.val)
            linkNode = linkNode.next
        res.append(linkNode.val)
        return res[::-1]

    '''
    方法二： 使用insert直接在头部插入
    '''
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead_2(self, linkNode: 'ListNode') -> 'ListNode':
        if not linkNode:
            return []
        res = []
        head = linkNode
        while head:
            res.insert(0, head.val)
            head = head.next
        return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    l1 = list_2_listnode(arr)
    a = Solution()
    res = a.printListFromTailToHead(l1)
    print(res)
    res = a.printListFromTailToHead_2(l1)
    print(res)
    arr = []
    l1 = list_2_listnode(arr)
    a = Solution()
    res = a.printListFromTailToHead(l1)
    print(res)
    res = a.printListFromTailToHead_2(l1)
    print(res)