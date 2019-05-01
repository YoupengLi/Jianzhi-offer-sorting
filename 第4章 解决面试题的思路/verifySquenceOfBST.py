# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 0019 下午 10:33
# @Author  : Youpeng Li
# @Site    : 
# @File    : verifySquenceOfBST.py
# @Software: PyCharm

'''
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回True,否则返回False。
假设输入的数组的任意两个数字都互不相同。
1. 二叉搜索树即是二叉排序树，二叉搜索树左子树上所有的结点均小于根结点、右子树所有的结点均大于根结点；
2. 后序遍历序列的最后一个元素为二叉树的根节点。
算法步骤如下：
1. 找到根结点；
2. 遍历序列，找到第一个大于等于根结点的元素i，则i左侧为左子树、i右侧为右子树；
3. 我们已经知道i左侧所有元素均小于根结点，那么再依次遍历右侧，看是否所有元素均大于根结点；若出现小于根结点的元素，则直接返回false；若右侧全都大于根结点，则：
4. 分别递归判断左/右子序列是否为后序序列；
'''

class Solution:
    def verifySquenceOfBST(self, seq: 'list[int]') -> 'bool':
        if not seq:
            return False
        root = seq[-1]
        i = 0
        for node in seq[:-1]:
            if node > root:
                break
            i += 1              # i为右子树第一个值的索引
        for node in seq[i:-1]:
            if node < root:
                return False

        # 判断左子树是否为二叉搜索树
        left = True
        # i>0 意味左树至少有一个元素:seq[0]
        if i > 0:
            left = self.verifySquenceOfBST(seq[:i])

        right = True
        # i<len(seq)-2 意味右树至少有一个元素：seq[len(seq)-2]
        if left and i < len(seq) - 2:
            right = self.verifySquenceOfBST(seq[i+1:-1])

        return left and right

if __name__ == "__main__":
    a = Solution()
    arr = [5, 7, 6, 9, 11, 10, 8]
    print(a.verifySquenceOfBST(arr))
    arr = [7, 4, 6, 5]
    print(a.verifySquenceOfBST(arr))