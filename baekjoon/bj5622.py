# -*- coding: utf-8 -*-
"""bj5622.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d5Ll7jMsL80oWa6C0_SdckzPJtk4Tqcs
"""

# no.5622 다이얼

al = input()

nd = {3:'ABC', 4:'DEF', 5:'GHI', 6:'JKL', 7:'MNO', 8:'PQRS', 9:'TUV', 10:'WXYZ'}
sol = 0

for x in al:
    for k, v in nd.items():
        if x in v:
            sol += k
            continue

print(sol)