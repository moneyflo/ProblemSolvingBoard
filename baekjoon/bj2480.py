# -*- coding: utf-8 -*-
"""bj2480.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14Jf9F2o18S0s_bY42yjQXxbWuidfLQwJ
"""

# no.2480 주사위 세개

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a*1000)
elif a == b or b == c or a == c:
    if a == b:
        print(1000 + a*100)
    elif b == c:
        print(1000 + b*100)
    else:
        print(1000 + a*100)
else:
    L = [a, b, c]
    L.sort()
    n = L[2]
    print(n * 100)