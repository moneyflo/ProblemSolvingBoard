# -*- coding: utf-8 -*-
"""bj23813.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d6OyAmRl1PoUtwZix0mh0UBS8pzIdnDm
"""

# no.23813 회전

N = int(input())
L = len(str(N))
s = 0
sol = 0

for x in str(N):
    s += int(x)

for i in range(L):
    sol += s * (10 ** i)

print(sol)

len('123')