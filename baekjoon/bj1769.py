# -*- coding: utf-8 -*-
"""bj1769.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ovrfi0v3JdLlrBrDtyPdv3FEDynmOe64
"""

# no.1769 3의 배수

X = list(map(int, list(input())))
mu = [3, 6, 9]
if len(X) == 1:
    if X[0] in mu:
        print(0)
        print('YES')
    else:
        print(0)
        print('NO')
else:
    x = sum(X)
    cnt = 1

    while 1:
        if x >= 10:
            x = sum(list(map(int, list(str(x)))))
            cnt += 1
        else:
            if x in mu:
                print(cnt)
                print('YES')
                break
            else:
                print(cnt)
                print('NO')
                break

x