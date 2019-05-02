# -*- coding: utf-8 -*-
# @Time    : 2019/1/26 0026 下午 9:08
# @Author  : Youpeng Li
# @Site    : 
# @File    : getTreeDepth.py
# @Software: PyCharm

'''
题目：输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

思路：利用递归实现。如果一棵树只有一个节点，那么它的深度为1。递归的时候无需判断左右子树是否存在，
因为如果该节点为叶节点，它的左右子树不存在，那么在下一级递归的时候，直接return 0。
同时，记得每次递归返回值的时候，深度加1操作，因为计算深度是从根节点下面一个节点开始计算的。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTreeDepth(self, pRoot: 'TreeNode') -> 'int':
        if pRoot == None:
            return 0
        return max(self.getTreeDepth(pRoot.left), self.getTreeDepth(pRoot.right)) + 1

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
    res = a.getTreeDepth(pRoot)
    print(res)