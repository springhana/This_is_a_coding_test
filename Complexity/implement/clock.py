# 시(H)를 입력받기
n = int(input())
count = 0

for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):  # str() <= 문자열로 변경
                count += 1

print(count)
