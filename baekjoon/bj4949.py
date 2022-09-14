# -*- coding: utf-8 -*-
"""bj4949.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vPy5JuywRktAy2xv9frdhUbOY3EsJ9VO
"""

# no.4949 균형잡힌 세상

def check(s):
    L = []
    for x in s:
        if x in ('(', '[', '{'):
            L.append(x)
        elif x in (')', ']', '}'):
            if not len(L):
                return 'no'
            else:
                left = L.pop()
                if x == ')' and left != '(' or \
                   x == ']' and left != '[' or \
                   x == '}' and left != '{':
                   return 'no'
    if len(L):
        return 'no'
    else:
        return 'yes'

while 1:
    s = input()
    if s == '.':
        break
    
    print(check(s))

a = 'asdad'
list(a)