# -*- coding: utf-8 -*-
"""bj4796.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iVuFy4fSfebxFDgLKUduA7YLOwMZEkQ-
"""

# no.4796 캠핑

sol = 0
cnt = 1
L, P, V = map(int, input().split())

while not (L == 0 and P == 0 and V == 0):
    sol = V // P * L
    di = V % P

    if di >= L:
        sol += L
    else:
        sol += di
    
    print(f"Case {cnt}: {sol}")
    cnt += 1
    L, P, V = map(int, input().split())