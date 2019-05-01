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
            i += 1
        for node in seq[i:-1]:
            if node < root:
                return False

        # 判断左子树是否为二叉搜索树
        left = True
        # i>0 意味i=0或者1的时候，两个元素在二叉树没有排序之分的，但是3个元素就有了左右子树之分
        if i > 0:
            left = self.verifySquenceOfBST(seq[:i])

        right = True
        # len(sequence)>3才有左右之分的
        if i < len(seq) - 2 and left:
            right = self.verifySquenceOfBST(seq[i + 1:])

        return left and right

if __name__ == "__main__":
    a = Solution()
    arr = [5, 7, 6, 9, 11, 10, 8]
    print(a.verifySquenceOfBST(arr))
    arr = [7, 4, 6, 5]
    print(a.verifySquenceOfBST(arr))
