# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 0011 上午 11:20
# @Author  : Youpeng Li
# @Site    : 
# @File    : lowestCommonAncestor_BT.py
# @Software: PyCharm

'''
题目：给定一棵二叉搜索树的根节点和两个节点，找到这两个节点的最低公共祖先节点。

解题思路：
从树的根节点开始，与两个输入节点进行比较。
<1> 如果当前节点的值比两个节点的值都大，则最低公共祖先节点一定在当前节点的左子树上；
<2> 如果当前节点的值比两个节点的值都小，则最低公共祖先节点一定在当前节点的右子树上；
<3> 如果一个节点比当前节点大或等于，另一个节点比当前节点小或等于，则最低公共祖先节点为当前节点。
该算法的时间复杂度为o(log n)，空间复杂度为o(1)。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor_BT(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None

        # 比根节点都小，到左子树中找
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor_BT(root.left, p, q)
        # 比根节点都大，到右子树中找
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor_BT(root.right, p, q)
        # 其他情况
        else:
            return root

if __name__ == "__main__":
    '''
            _______8_______
           /               \
       ___6___          ___10___
      /       \        /        \
     5         7      9         11
    '''
    t1 = TreeNode(8)
    t2 = TreeNode(6)
    t3 = TreeNode(10)
    t4 = TreeNode(5)
    t5 = TreeNode(7)
    t6 = TreeNode(9)
    t7 = TreeNode(11)

    t1.left = t2
    t1.right = t3

    t2.left = t4
    t2.right = t5

    t3.left = t6
    t3.right = t7

    root = t1

    a = Solution()
    res = a.lowestCommonAncestor_BT(root, t6, t7)
    print(res.val)