# -*- coding: utf-8 -*-
"""bj5347.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aPnwrJsqrUW6koCw6_Ji_Ja13803dbKF
"""

# no.5347 LCM

import math

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    print(math.lcm(a, b))