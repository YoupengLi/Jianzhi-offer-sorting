# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 0011 下午 8:27
# @Author  : Youpeng Li
# @Site    : 
# @File    : lowestCommonAncestor_NormalTree.py
# @Software: PyCharm

'''
题目：给定一棵普通树的根节点和两个节点，找到这两个节点的最低公共祖先节点。

解题思路：
方法一：用两个链表分别保存从根节点到输出的两个节点的路径，然后把问题转化成两个链表的最后公共节点的问题。
时间复杂度：为了得到从根节点开始到输入的两个节点的两条路径，需要遍历两次树，每遍历一次的时间复杂度为o(n)，
得到两条路径的长度最差为o(n)，通常两条路径为o(log n)。
总体时间复杂度为o(n)。

方法二：
<1> 如果两个节点分别在根节点的左子树和右子树，则返回根节点；
<2> 如果两个节点都在左子树，则递归处理左子树；
<3> 如果两个节点都在右子树，则递归处理右子树。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 判断节点是否在树中
    def findNode(self, root: 'TreeNode', p: 'TreeNode') -> 'bool':
        if not root or not p:
            return False

        res = False
        if root.val == p.val:
            return True
        if not res:
            res = self.findNode(root.left, p)
        if not res:
            res = self.findNode(root.right, p)
        return res

    def lowestCommonAncestor_NormalTree(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None

        if root.val == p.val or root.val == q.val:
            return root
        # 判断节点p是否在左子树中
        if self.findNode(root.left, p):
            if self.findNode(root.right, q):
                return root
            # 两个节点都在左子树中
            else:
                return self.lowestCommonAncestor_NormalTree(root.left, p, q)

        # 说明p在右子树中
        else:
            if self.findNode(root.left, q):
                return root
            # 两个节点都在右子树中
            else:
                return self.lowestCommonAncestor_NormalTree(root.right, p, q)

if __name__ == "__main__":
    '''
                  _______A_______
                 /               \
            ____B____             C
           /         \ 
        __D__       __E__
       /     \     /     \
      F       G   H       I
    '''
    t1 = TreeNode('A')
    t2 = TreeNode('B')
    t3 = TreeNode('C')
    t4 = TreeNode('D')
    t5 = TreeNode('E')
    t6 = TreeNode('F')
    t7 = TreeNode('G')
    t8 = TreeNode('H')
    t9 = TreeNode('I')

    t1.left = t2
    t1.right = t3

    t2.left = t4
    t2.right = t5

    t4.left = t6
    t4.right = t7

    t5.left = t8
    t5.right = t9

    root = t1

    a = Solution()
    res = a.lowestCommonAncestor_NormalTree(root, t2, t8)
    print(res.val)