# 직접 데이터를 넣어 초기화
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 네 번째 원소만 출력
print(a[3])

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n  # 배열 값이 모두 0이고 길이가 10
print(a)

# 여덟 번째 원소만 출력
print(a[7])

# 뒤에서 첫 번째 원소 출력
print(a[-1])  # 8

# 뒤에서 세 번째 원소 출력
print(a[-3])  # 7

# 네 번째 원소 값 변경
a[3] = 7
print(a)  # [1.2.3.7.5.6.8.9]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])

# 0 부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 일반적인 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

# 1부터 9까지의 수들을 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

# N X M 크기의 2차원 리스트 초기화 (잘못된 방법)
n = 4
m = 3
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)

# 리스트 관련 기타 메서드
a = [1, 4, 3]
print("기본 리스트:", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입:", a)

# 오름차순 정렬
a.sort()
print("오름차순:", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순:", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기:", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3추가:", a)

# 특정 값이 데이터 개수 세기
print("값이 3인 데이터 개수:", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제:", a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}  # 집합 자료형

# remove_list에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)
