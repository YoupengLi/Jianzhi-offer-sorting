# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 0012 下午 4:56
# @Author  : Youpeng Li
# @Site    : 
# @File    : rebuildBinaryTree.py
# @Software: PyCharm

'''
题目：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rebuildBinaryTree(self, pre: 'List[int]', ino: 'List[int]') -> 'List[int]':
        # Construct Binary Tree from Preorder and Inorder Traversal
        # 根据前序和中序来构建二叉树
        if pre == []:
            return None
        val = pre[0]
        idx = ino.index(val)
        lino = ino[0:idx]
        rino = ino[idx + 1:]
        lpre = pre[1:1 + len(lino)]
        rpre = pre[1 + len(lino):]
        root = TreeNode(val)
        root.left = self.rebuildBinaryTree(lpre, lino)
        root.right = self.rebuildBinaryTree(rpre, rino)
        return root

    def rebuildBinaryTree_2(self, ino: 'List[int]', pos: 'List[int]') -> 'List[int]':
        # Construct Binary Tree from Inorder and Postorder Traversal
        # 根据中序和后序构建二叉树
        if pos == []:
            return None
        val = pos[-1]
        idx = ino.index(val)
        lino = ino[0:idx]
        rino = ino[idx+1:]
        lpos = pos[0:len(lino)]
        rpos = pos[len(lino):-1]
        root = TreeNode(val)
        root.left = self.rebuildBinaryTree(lino, lpos)
        root.right = self.rebuildBinaryTree(rino, rpos)
        return root

if __name__ == "__main__":
    '''
                  _______1_______
                 /               \
            ____2             ____3____
           /                 /         \ 
          4__               5         __6
             \                       /
              7                     8
    '''
    a = Solution()
    l1 = [1, 2, 4, 7, 3, 5, 6, 8]  # 前序遍历
    l2 = [4, 7, 2, 1, 5, 3, 8, 6]  # 中序遍历
    l3 = [7, 4, 2, 5, 8, 6, 3, 1]  # 后序遍历
    res = a.rebuildBinaryTree(l1, l2)
    print(res.val)
    res = a.rebuildBinaryTree_2(l2, l3)
    print(res.val)