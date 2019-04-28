# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 下午 8:21
# @Author  : Youpeng Li
# @Site    : 
# @File    : minNumberInRotateArray.py
# @Software: PyCharm

'''
题目：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，输出旋转数组的
最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
Note：给出的所有元素都大于0，若数组大小为0，请返回0。

（1）考虑数字没有重复的情况
使用二分法，有两个指针，第一个指针指向front，第二个指针指向rear，midIndex是中间数字，
只要是旋转数组，那么首位一定大于末位。
如果中间位元素大于等于首位，将第一个指针指向中间位（最小元素在后半段）；
如果中间位元素小于等于首位，将第二个指针指向中间位（最小元素在前半段）；
不断迭代，当首位和最后位只差1时，最后位就是最小值，此时最坏时间复杂度是O(logn)。
（2）考虑数字有重复的情况
eg:[1,0,1,1,1]  [1,1,1,0,1]
使用顺序查找方式。
'''

class Solution:
    def minNumberInRotateArray(self, rotArr: 'list[int]') -> 'int':
        if not rotArr or len(rotArr) <= 0:
            return 0

        front, rear = 0, len(rotArr) - 1
        midIndex = front
        while rotArr[front] >= rotArr[rear]:
            if rear - front == 1:
                midIndex = rear
                break
            midIndex = (front + rear) // 2
            if rotArr[front] == rotArr[midIndex] and rotArr[front] == rotArr[rear]:
                return self.minOrder(rotArr, front, rear)

            if rotArr[front] <= rotArr[midIndex]:
                front = midIndex
            elif rotArr[rear] >= rotArr[midIndex]:
                rear = midIndex
        return rotArr[midIndex]

    def minOrder(self, arr: 'list[int]', front: 'int', end: 'int') -> 'int':
        res = arr[0]
        for i in arr[front:end + 1]:
            if i < res:
                res = i
        return res

if __name__== "__main__":
    a = Solution()
    arr = [3, 4, 5, 1, 2]
    print(a.minNumberInRotateArray(arr))
    arr = [2, 5, 2, 2, 2]
    print(a.minNumberInRotateArray(arr))