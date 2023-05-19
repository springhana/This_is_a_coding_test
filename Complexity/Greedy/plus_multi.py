data = input()
# 첫번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):  # 여기서 1은 data에 인덱스 1번을 표현
    # 두 수중에서 하나라도 ‘0’ 혹은 ‘1’ 인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])  # 문자를 숫자로 변경하여 num에 대입
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
