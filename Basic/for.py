i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print(result)

# 무한 루프
# x = 10
# while x > 5:
#     print(x)

array = [9, 2, 4, 5, 6]
for x in array:
    print(x)

result = 0
# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
    result += i

print(result)

# continue
result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i

print(result)

# break
i = 1

while True:
    print("현재 i의 값:", i)
    if i == 5:
        break
    i += 1

# 중첩된 반복문
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()
