# -*- coding: utf-8 -*-
"""bj17478.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hkmAVr9Ujnu6L9Ab8RbxxvMt_EVn4FXU
"""

# no,17478 재귀함수가 뭔가요?

N = int(input())
cnt = 0

def what(n, cnt):
    cnt += 1
    if cnt != N:
        print(4*cnt*'_' + '"재귀함수가 뭔가요?"')
        print(4*cnt*'_' + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(4*cnt*'_' + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(4*cnt*'_' + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        what(n-1, cnt)
        print(4*cnt*'_' + '라고 답변하였지.')
    else:
        print(4*cnt*'_' + '"재귀함수가 뭔가요?"')
        print(4*cnt*'_' + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(4*cnt*'_' + '라고 답변하였지.')
        return


print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
print('"재귀함수가 뭔가요?"')
print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
print('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

what(N, cnt)

print('라고 답변하였지.')