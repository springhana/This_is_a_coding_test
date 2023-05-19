# N,M,K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())  # N은 배열 크기, M은 더할 횟수, K는 연속으로 사용되는 횟수
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

result = 0  # 더한 수를 받을 값

# 배열 정렬
data.sort()
# 첫 번째로 큰수
first_max = data[N - 1]
# 두 번째로 큰수
second_max = data[N - 2]

while True:
    # 1세트
    for i in range(K):  # 가장 큰 수를 K번 더하기 : range(k) 순차적으로 반복
        if M == 0:
            break
        result += first_max  # K 번만큼 더하기
        M -= 1  # 더할 횟수를 하나씩 빼기
    if M == 0:
        break
    result += second_max
    M -= 1  # 더할 횟수를 하나 빼기

print(result)
