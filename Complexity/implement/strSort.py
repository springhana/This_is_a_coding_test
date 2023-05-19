data = input()  # 문자열 입력받기
result = []  # 최종 결과를 담을 리스트
value = 0  # 숫자를 담을 변수

for x in data:  # 문자열 길이 만큼 반복
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():  # x가 알파벳이면!
        result.append(x)  # 리스트에 추가
    # 숫자는 따로 더하기
    else:
        value += int(x)  # 숫자이면 value에 담기

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 반환하여 출력)
print(''.join(result))
