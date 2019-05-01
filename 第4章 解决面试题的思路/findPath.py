# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 0020 下午 11:46
# @Author  : Youpeng Li
# @Site    : 
# @File    : findPath.py
# @Software: PyCharm

'''
题目：输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
路径定义为从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

思路：
递归先序遍历树， 把节点加入路径。使用列表结构存储树结构。
若该节点是叶子节点，则比较当前路径和是否等于期待和，叶子节点说明该路径已经截止了。
弹出节点，每一轮递归返回到父节点时，当前路径也应该回退一个节点。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def findPath(self, root: 'TreeNode', expectNum: 'int') -> 'list[list[int]]':
        if not root:
            return []
        res = []

        def findPath2(root: 'TreeNode', path: 'list[list[int]]', currentNum: 'int'):
            currentNum += root.val
            path.append(root)
            # 判断是不是到叶子节点
            flag = root.left == None and root.right == None
            if currentNum == expectNum and flag:
                onepath = []
                for node in path:
                    onepath.append(node.val)
                res.append(onepath)

            if currentNum < expectNum:
                if root.left:
                    findPath2(root.left, path, currentNum)
                if root.right:
                    findPath2(root.right, path, currentNum)
            # 拿到一个正确的路径后要弹出，回到上一次父节点继续递归
            path.pop()

        findPath2(root, [], 0)
        return res

if __name__ == "__main__":
    '''
           ____10____
          /          \ 
       __5__         12
      /     \   
     4       7  
    '''
    t1 = TreeNode(10)
    t2 = TreeNode(5)
    t3 = TreeNode(12)
    t4 = TreeNode(4)
    t5 = TreeNode(7)

    t1.left = t2
    t1.right = t3

    t2.left = t4
    t2.right = t5

    root = t1

    a = Solution()
    res = a.findPath(root, 22)
    [print(i) for i in res]