# -*- coding: utf-8 -*-
"""bj2675.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A4_9XB7JEe8ijQcAy0in_Gc1LKdijYg3
"""

# no.2675 문자열 반복

T = int(input())

for _ in range(T):
    r, s = input().split()
    r = int(r)
    sol = ''
    for x in s:
        sol += x * r
    
    print(sol)

'' + 'asd' + '' + 'casd'