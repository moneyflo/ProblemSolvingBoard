# -*- coding: utf-8 -*-
"""bj1920.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S6ZGFH0pMezUhVH9YkfnU7R3WSXEGdmT
"""

# 수 찾기

N = int(input())
l_n = list(map(int, input().split()))
l_n.sort()
M = int(input())
l_m = list(map(int, input().split()))


def half(list1, x):
    l1 = []
    length = len(list1)
    if length < 100:
        l1 = list1
        return l1
    else:
        if x < list1[length//2]:
            l1 = list1[:length//2 + 1]
            return l1
        else:
            l1 = list1[length//2+1:]
            return l1




for i in range(M):
    n1 = l_m[i]
    l2 = l_n
    while len(l_n) > 100:
        l2 = half(l_n, l_m[i])
    if l_m[i] in l2:
        print(1)
    else:
        print(0)

# 두번째 시도

N = int(input())
s1 = list(map(int, input().split()))

M = int(input())
s2 = list(map(int, input().split()))

ss = list(set(s1) & set(s2))

for x in s2:
    if x in ss:
        print(1)
    else:
        print(0)

# 세번째 시도
N = input()
s1 = set(input().split())
M = input()
s2 = input().split()

for x in s2:
    if x in s1:
        print(1)
    else:
        print(0)