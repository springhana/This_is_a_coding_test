from collections import Counter
from itertools import combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']  # 데이터 준비

result = list(combinations(data, 2))  # 2개를 뽑는 모든 조합 구하기
print(result)

result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

result = list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

# Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # 'blue'가 등장한 횟수 출력
print(counter['green'])  # 'green'가 등장한 횟수 출력
print(dict(counter))  # 사전 자료형으로 반환

# 최대 공약수와 최소 공배수
import math


# 최소 공배수 (LCM)를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)


a = 21
b = 14

print(math.gcd(21, 14))  # 최대 공약수 (GCD) 계산
print(lcm(21, 14))  # 최소 공배수(LCM) 계산
