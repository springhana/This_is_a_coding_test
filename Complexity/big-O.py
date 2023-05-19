# 시간 복잡도를 표현할 때는 빅오(Big-O)표기법

array = [3, 5, 1, 2, 4]  # 5개의 데이터 (N=5) <= 가장 영향력이 큰 부븐은 N에 비례하는 연산을 수행하는 반복문 부분이므로 시간복잡도를 O(N)이라고 표기
summary = 0  # 합계를 저장할 변수

# 모든 데이터를 하나씩 확인하며 합계를 계산
for x in array:
    summary += x

# 결과를 출력
print(summary)
print("\n")

a = 5
b = 7
print(a + b)  # 단순한 더하기 연산 한 번이 수행 <= 상수 연산이므로 시간 복잡도는 O(1)로 표현
print("\n")

array = [3, 5, 1, 2, 4]  # 5개의 데이터 (N=5)

# 2중 반복문을 이용하여 각 원소에 대하여 다른 모든 원소에 대한 곱셉 결과를 매번 출력하고 있기때문에 O(N^2)의 시간복잡도 but 모든 2중 반복문이 O(N^2)가 아니다.
for i in array:
    for j in array:
        temp = i * j
        print(temp)
