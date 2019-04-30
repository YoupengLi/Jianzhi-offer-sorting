# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 下午 4:30
# @Author  : Youpeng Li
# @Site    : 
# @File    : reverseList.py
# @Software: PyCharm

'''
题目：输入一个链表，反转链表后并输出反转后链表的头节点。
例如 1->2->3->4->5  ==>  5->4->3->2->1

tmp = pHead.next   把当前节点的下一个节点保存下来
pHead.next = pre   把前一个节点移到当前节点的下一个节点，因为要翻转节点，pre始终指向要反转节点的首节点
pre = pHead        当前节点向后移一位
pHead = tmp        把之前保存的下一个节点指针再给当前节点接着翻转
'''

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def list_2_linknode(arr: 'list[int]') -> 'ListNode':
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
    def reverseList(self, pHead: 'ListNode') -> 'ListNode':
        if not pHead or not pHead.next:
            return pHead
        pre = None
        while pHead:
            tmp = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = tmp
        return pre

if __name__ == "__main__":
    a = Solution()
    arr = [1, 2, 3, 4, 5]
    l1 = list_2_linknode(arr)
    res = a.reverseList(l1)
    print(res)