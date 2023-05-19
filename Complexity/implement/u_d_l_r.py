# N 입력 받기
n = int(input())  # 행과 열 정하기
x, y = 1, 1  # 시작 위치
plans = input().split()  # 입력받을 상,하,좌,우

# L,R,U,D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):  # move_types 개수 만큼
        if plan == move_types[i]:  # 하나씩 입력받은 plans랑 비교
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
