# -*- coding: utf-8 -*-
"""bj11134.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qjJL9ucd0TPS9TAH4kmUZan9_VAkuKYo
"""

# no.11134 쿠키애호가

T = int(input())

for _ in range(T):
    n, c = map(int, input().split())

    if not n % c:
        print(n//c)
    else:
        print(n//c+1)