# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 0018 上午 8:33
# @Author  : Youpeng Li
# @Site    : 
# @File    : mirror.py
# @Software: PyCharm

'''
题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。
eg:
           ____8____                          ____8____
          /         \                        /         \
       __6__      __10__    ——————>       __10__      __6__
      /     \    /      \                /      \    /     \
     5       7   9      11              11       9  7       5

思路：
先前序遍历这棵树的每个节点，如果遍历到的节点有子节点，就交换它的两个子节点。
当交换完所有的非叶子节点的左右子节点之后，就得到了该树的镜像。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def mirror(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)
        return root

if __name__ == "__main__":
    '''
           ____8____                          ____8____
          /         \                        /         \
       __6__      __10__    ——————>       __10__      __6__
      /     \    /      \                /      \    /     \
     5       7   9      11              11       9  7       5
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
    res = a.mirror(root)
    print(res.val)