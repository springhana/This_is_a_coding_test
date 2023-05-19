# 함수
def add(a, b):
    return a + b


print(add(3, 7))


# 함수 2
def add(a, b):
    print(a + b)


add(3, 7)


# 매개변수 순서가 달라도 상관없음
def add(a, b):
    print(a + b)


add(b=3, a=7)

# global
a = 0


def func():
    global a
    a += 1


for i in range(10):
    func()

print(a)


# 여러 개의 반환 값
def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var


a, b, c, d, = operator(7, 3)  # 반환 값이 4개니간 변수도 4개
print(a, b, c, d)


# 람다식

def add(a, b):
    return a + b


# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))

# 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
print(list(result))

# 내장 함수
# sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval()
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('이무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)
