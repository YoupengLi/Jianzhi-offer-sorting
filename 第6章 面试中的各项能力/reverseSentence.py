# -*- coding: utf-8 -*-
# @Time    : 2019/2/6 0006 上午 8:57
# @Author  : Youpeng Li
# @Site    : 
# @File    : reverseSentence.py
# @Software: PyCharm

'''
题目：牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容
颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把
句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

思路：首先需要写一个reverse函数，把任何输入的字符串完全翻转。然后从前往后依次遍历新字符串，如果遇到空格，
就把空格前的字符串用reverse翻转，添加空格，继续遍历。需要注意的是，如果新字符串结尾不是空格，当遍历到结尾的
时候，前一个空格到结尾的字符串没有翻转，因此记得跳出遍历后，需要再完成一次翻转操作。
举例：
                student. a am I
                I ma a .tneduts
                I                    pEnd = ' ',首先让空格前面的字符进行翻转，然后 pStart = pEnd
                  am                 pStart = ' ',两个指针都向前进到a位，下一次pEnd继续向前进到空格为止，然后ma翻转变成am
                     a
                       student.      同理
<1> 从头开始，pStart = pEnd = 0，pEnd向后找到' '
<2> 将pStart~pEnd反转并添加到结果中，更新pStart = pEnd
<3> 此时pStart = ' '，更新pStart、pEnd（+1），并将' ' 添加到结果中
<4> 直到pEnd = len(s)-1（最后一位），将pStart~pEnd反转并添加到结果中。
'''
class Solution:
    def reverseSentence(self, s: 'str') -> 'str':
        if not s or len(s) <= 0:
            return ""

        s = list(s)
        s = self.reverse(s)
        pStart = 0
        pEnd = 0
        listTemp = []
        res = ""
        while pEnd < len(s):
            if pEnd == len(s) - 1:
                listTemp.append(self.reverse(s[pStart:]))
                break
            if s[pStart] == ' ':
                pStart += 1
                pEnd += 1
                listTemp.append(' ')

            elif s[pEnd] == ' ':
                listTemp.append(self.reverse(s[pStart:pEnd]))
                pStart = pEnd
            else:
                pEnd += 1
        for i in listTemp:
            res += ''.join(i)
        return res

    def reverse(self, s: 'list[char]') -> 'list[char]':
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s

if __name__ == "__main__":
    a = Solution()
    s = "student. a am I"
    res = a.reverseSentence(s)
    print(res)