# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 下午 8:53
# @Author  : Youpeng Li
# @Site    : 
# @File    : hasSubtree.py
# @Software: PyCharm

'''
题目：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

分析:首先判断根节点是不是相同，如果根节点相同，那么进入判断是否相同的函数；
如果不相同，接着递归判断左边子树与B是不是相同；
如果还不相同，接着递归判断右边子树与B是不是相同。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasSubtree(self, pRoot1: 'TreeNode', pRoot2: 'TreeNode') -> 'TreeNode':
        result = False
        if pRoot1 != None and pRoot2 != None:
            # 判断根节点
            if pRoot1.val == pRoot2.val:
                result = self.same(pRoot1, pRoot2)
            # 判断左子树
            if not result:
                result = self.hasSubtree(pRoot1.left, pRoot2)
            # 判断右子树
            if not result:
                result = self.hasSubtree(pRoot1.right, pRoot2)
        return result

    def same(self, pRoot1: 'TreeNode', pRoot2: 'TreeNode') -> 'bool':
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.same(pRoot1.left, pRoot2.left) and self.same(pRoot1.right, pRoot2.right)

if __name__ == "__main__":
    '''
                  _______8_______                   ___8___
                 /               \                 /       \
            ____8____             7               9         2
           /         \ 
          9         __2__
                   /     \
                  4       7
    '''
    t1 = TreeNode(8)
    t2 = TreeNode(8)
    t3 = TreeNode(7)
    t4 = TreeNode(9)
    t5 = TreeNode(2)
    t6 = TreeNode(4)
    t7 = TreeNode(7)

    t1.left = t2
    t1.right = t3

    t2.left = t4
    t2.right = t5

    t5.left = t6
    t5.right = t7

    pRoot1 = t1

    t11 = TreeNode(8)
    t12 = TreeNode(9)
    t13 = TreeNode(2)

    t11.left = t12
    t11.right = t13

    pRoot2 = t11

    a = Solution()
    res = a.hasSubtree(pRoot1, pRoot2)
    print(res)