# 데이터의 개수 입력
n = int(input())  # 정수로 받음, 입력
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 적은 수의 데이터
a, b, c = map(int, input().split())
print(a, b, c)

import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)

# 출력할 변수들
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")

# 출력할 변수
answer = 7
print("정답은 " + str(answer) + "입니다.")  # str문자열로 바꿈
print(f"정답은 {answer}입니다.")