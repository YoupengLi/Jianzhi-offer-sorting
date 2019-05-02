# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 0021 下午 10:31
# @Author  : Youpeng Li
# @Site    : 
# @File    : convertFromBSTToList.py
# @Software: PyCharm

'''
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    解题思路一：中序遍历，将所有的节点保存到一个列表中，对这个list[:-1]进行遍历，
    每个节点的right设为下一个节点，下一个节点的left设为上一个节点。
    借助了一个O(n)的辅助空间。
    '''
    def convertFromBSTToList(self, pRootOfTree: 'TreeNode') -> 'TreeNode':
        if not pRootOfTree:
            return
        self.attr = []
        self.inOrder(pRootOfTree)

        for i, v in enumerate(self.attr[:-1]):
            self.attr[i].right = self.attr[i + 1]
            self.attr[i + 1].left = v

        return self.attr[0]

    def inOrder(self, root: 'TreeNode'):
        if not root:
            return
        self.inOrder(root.left)
        self.attr.append(root)
        self.inOrder(root.right)

    '''
    解题思路二：递归，将特定节点的左指针指向其左子树中的最后子节点，
    将其右指针指向其右子树中的最左子节点，依次递归，调整好全部节点的指针指向。
    '''
    def convertFromBSTToList_1(self, pRootOfTree: 'TreeNode') -> 'TreeNode':
        if not pRootOfTree:
            return
        root = pHead = pRootOfTree
        # 找到根节点
        while pHead.left:
            pHead = pHead.left
        self.core(root)
        return pHead

    def core(self, root: 'TreeNode'):
        if not root.left and not root.right:
            return
        if root.left:
            # 找到左子树中的最右子节点
            preRoot = root.left
            self.core(root.left)
            while preRoot.right:
                preRoot = preRoot.right
            preRoot.right = root
            root.left = preRoot
        if root.right:
            # 找到右子树中的最左子节点
            nextRoot = root.right
            self.core(root.right)
            while nextRoot.left:
                nextRoot = nextRoot.left
            nextRoot.left = root
            root.right = nextRoot

if __name__ == "__main__":
    '''
           ____10____ 
          /          \ 
       __6__       __14__ 
      /     \     /      \
     4       8   12      16
    '''
    t1 = TreeNode(10)
    t2 = TreeNode(6)
    t3 = TreeNode(14)
    t4 = TreeNode(4)
    t5 = TreeNode(8)
    t6 = TreeNode(12)
    t7 = TreeNode(16)

    t1.left = t2
    t1.right = t3

    t2.left = t4
    t2.right = t5

    t3.left = t6
    t3.right = t7

    root = t1

    a = Solution()
    res = a.convertFromBSTToList(root)
    print(res.val)


    t1 = TreeNode(10)
    t2 = TreeNode(6)
    t3 = TreeNode(14)
    t4 = TreeNode(4)
    t5 = TreeNode(8)
    t6 = TreeNode(12)
    t7 = TreeNode(16)

    t1.left = t2
    t1.right = t3

    t2.left = t4
    t2.right = t5

    t3.left = t6
    t3.right = t7

    root = t1

    res = a.convertFromBSTToList_1(root)
    print(res.val)