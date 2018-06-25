# -*- coding:utf-8 -*-
#!/usr/bin/python
import math


def scoreOfParentheses(S):
    """
    :type S: str
    :rtype: int
    """
    s=str(S)
    if '()' in s:
        s = s.replace('()', '*')
    tem = 0
    while True:
        for i in range(pow(2, 13)):
            m = '*'*i
            m = '(' +m + ')'
            if m in s:
                s = s.replace(m,  '*'*i*2)
        tem += 1
        if tem == 10:
            break
    #print s
    print len(s)
    return None

def fun(S):
    S = S[1:-1]
    if S == '':
        return 1
    return fun2(S)*2

def fun2(S):
    flag = 0
    sum = 0
    index = 0
    for j, i in enumerate(S):
        if i == '(':
            flag += 1
        if i == ')':
            flag -= 1
        if flag == 0:
            sum += fun(S[index:j + 1])
            index = j + 1
    return sum

S = "()()()(()())"
#scoreOfParentheses(S)
print fun2(S)



