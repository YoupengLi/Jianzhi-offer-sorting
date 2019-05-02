# -*- coding: utf-8 -*-
# @Time    : 2019/1/26 0026 下午 9:49
# @Author  : Youpeng Li
# @Site    : 
# @File    : isBalancedBinaryTree.py
# @Software: PyCharm

'''
题目：输入一棵二叉树，判断该二叉树是否是平衡二叉树。

平衡二叉树：平衡二叉搜索树（Balanced Binary Tree）具有以下性质：
它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
思路：如果二叉树的每个节点的左子树和右子树的深度不大于1，它就是平衡二叉树。
先写一个求深度的函数，再对每一个节点判断，看该节点的左子树的深度和右子树的深度的差是否大于1。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalancedBinaryTree(self, pRoot: 'TreeNode') -> 'bool':
        if pRoot == None:
            return True
        depth1 = self.getTreeDepth(pRoot.left)
        depth2 = self.getTreeDepth(pRoot.right)
        if abs(depth1 - depth2) > 1:
            return False
        return self.isBalancedBinaryTree(pRoot.left) and self.isBalancedBinaryTree(pRoot.right)

    def getTreeDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        return max(self.getTreeDepth(root.left), self.getTreeDepth(root.right)) + 1

if __name__ == "__main__":
    '''
                  _______1_______ 
                 /               \ 
            ____2____             3____
           /         \                 \ 
          4         __5                 6
                   /  
                  7 
    '''
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)

    t1.left = t2
    t1.right = t3

    t2.left = t4
    t2.right = t5

    t3.right = t6

    t5.left = t7

    pRoot = t1

    a = Solution()
    res = a.isBalancedBinaryTree(pRoot)
    print(res)