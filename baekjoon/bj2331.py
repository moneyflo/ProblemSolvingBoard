# -*- coding: utf-8 -*-
"""bj2331.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GYQrjSZljfs4b4wkgQhrdyg-UiGwH0XQ
"""

# no.2331 반복수열

A, P = map(int, input().split())

sq = [A]

for _ in range(9999):
    tmp1 = list(str(sq[-1]))
    tmp2 = 0
    for x in tmp1:
        tmp2 += pow(int(x), P)
    sq.append(tmp2)

print(len(set(sq[:len(sq)//2])) - len(set(sq[len(sq)//2:])))