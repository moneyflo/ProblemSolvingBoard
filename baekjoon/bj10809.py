# -*- coding: utf-8 -*-
"""bj10809.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D1XKd9bj1tncgRFf5v7UgsmEp_ZGjpnK
"""

# no.10809 알파벳 찾기

s = input()
apb = [-1] * 26
a = 'abcdefghijklmnopqrstuvwxyz'

for x in a:
    if x in s:
        tmp = a.find(x)
        if apb[tmp] == -1:
            apb[tmp] = s.find(x)

for x in apb:
    print(x, end=' ')