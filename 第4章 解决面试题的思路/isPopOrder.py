# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 0019 下午 4:37
# @Author  : Youpeng Li
# @Site    : 
# @File    : isPopOrder.py
# @Software: PyCharm

'''
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字
均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就
不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

三个栈，一个是压栈pushV，一个是出栈popV，一个是辅助栈stack，
把数据从pushV向stack中压，如果压入数据和出栈popV的栈顶元素一致，就从pushV和popV中同时弹出去。
然后再判断stack中最后一个元素和popV中第一个元素是否相同，若相同，则从stack和popV中同时弹出去。
等到pushV中元素全弹出来之后，判断popV中元素是否全部弹出，如果是，则说明是弹出序列，反之则不是。
入栈1,2,3,4,5
出栈4,5,3,2,1
首先1入辅助栈，此时栈顶1≠4，继续入栈2
此时栈顶2≠4，继续入栈3
此时栈顶3≠4，继续入栈4
此时栈顶4＝4，出栈4，弹出序列向后一位，此时为5，辅助栈里面是1，2，3
此时栈顶3≠5，继续入栈5
此时栈顶5=5，出栈5,弹出序列向后一位，此时为3，辅助栈里面是1，2，3
......
依次执行，最后辅助栈为空。如果不为空说明弹出序列不是该栈的弹出顺序。

栈的弹出序列的规律：
<1> 如果下一个弹出的数字刚好是栈顶数字，那么直接弹出；
<2> 如果下一个弹出的数字不在栈顶，我们把压栈序列中还没有入栈的数字压入辅助栈，直到把下一个需要弹出的数字压入栈顶即可；
<3> 如果所有的数字都压入栈了仍然没有找到下一个弹出的数字，那么该序列不可能是一个弹出序列。

'''

class Solution:
    def isPopOrder(self, pushV: 'list[int]', popV: 'list[int]') -> 'bool':
        stack = []
        while popV:
            # 如果第一个元素都相同，就直接弹出
            if pushV and pushV[0] == popV[0]:
                popV.pop(0)
                pushV.pop(0)
            # 如果stack中最后一个元素和popV中第一个元素相同
            elif stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True

if __name__ == "__main__":
    a = Solution()
    stack1 = [1, 2, 3, 4, 5]
    stack2 = [4, 5, 3, 2, 1]
    stack3 = [4, 3, 5, 1, 2]
    print(a.isPopOrder(stack1, stack2))
    print(a.isPopOrder(stack1, stack3))
