# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 下午 7:31
# @Author  : Youpeng Li
# @Site    : 
# @File    : mergeTwoLists.py
# @Software: PyCharm

'''
题目：输入两个单调递增排序的链表，合并这两个链表并使新链表中的节点仍然是按照递增排序的。
例如输入链表1和链表2，则合并之后的链表如链表3所示。
链表1：1 -> 3 -> 5 -> 7
链表2：2 -> 4 -> 6 -> 8
链表3：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
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
    def mergeTwoLists(self, p1: 'ListNode', p2: 'ListNode') -> 'ListNode':
        if p1 == None:
            return p2
        elif p2 == None:
            return p1

        merge_head = None
        if p1.val <= p2.val:
            merge_head = p1
            merge_head.next = self.mergeTwoLists(p1.next, p2)
        elif p1.val > p2.val:
            merge_head = p2
            merge_head.next = self.mergeTwoLists(p1, p2.next)

        return merge_head

if __name__ == "__main__":
    a = Solution()
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 6, 8, 10]
    l1 = list_2_listnode(arr1)
    l2 = list_2_listnode(arr2)
    list = a.mergeTwoLists(l1, l2)
    print(list.val)