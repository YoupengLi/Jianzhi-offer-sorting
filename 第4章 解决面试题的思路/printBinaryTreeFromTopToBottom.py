# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 0019 下午 8:10
# @Author  : Youpeng Li
# @Site    : 
# @File    : printBinaryTreeFromTopToBottom.py
# @Software: PyCharm

'''
题目：从上往下打印出二叉树的每个节点，同层节点从左至右打印

广度优先层次遍历，利用一个队列来实现
层序遍历的基本过程是：
先根节点入队，然后：
1.从队列中取出一个元素
2.访问该元素所指的结点
3.若该元素所指结点的左、右孩子结点非空，则将其左、右孩子的指针顺序入队
利用队列，首先将根节点放入队列中，取队列的首节点，把值存进列表，然后考虑左右指针，把指针放进列表，再存值
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表
    def printBinaryTreeFromTopToBottom(self, root: 'TreeNode') -> 'list[int]':
        if not root:
            return []
        queue = []
        res = []

        queue.append(root)
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

if __name__ == "__main__":
    '''
           ____8____
          /         \ 
       __6__      __10__
      /     \    /      \ 
     5       7   9      11
    '''
    t1 = TreeNode('8')
    t2 = TreeNode('6')
    t3 = TreeNode('10')
    t4 = TreeNode('5')
    t5 = TreeNode('7')
    t6 = TreeNode('9')
    t7 = TreeNode('11')

    t1.left = t2
    t1.right = t3

    t2.left = t4
    t2.right = t5

    t3.left = t6
    t3.right = t7

    root = t1

    a = Solution()
    res = a.printBinaryTreeFromTopToBottom(root)
    [print(i) for i in res]