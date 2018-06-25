# -*- coding:utf-8 -*-
import math

def buddyStrings(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    if len(A) != len(B):
        return False
    if len(A)==0 and len(B)==0:
        return False

    index = []
    for i, a in enumerate(A):
        if B[i] != a:
            index.append(i)
    for i, j in enumerate(index):
        if A[j] != B[index[len(index) - i - 1]]:
            return False

    if A == B:
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                if(i != j and a == b):
                    return True
    return True
A = "abab"
B = "abab"
print buddyStrings(A, B)
