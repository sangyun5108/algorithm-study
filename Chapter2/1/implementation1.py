n = int(input())
plans = list(input().split())

x = 1
y = 1

# 왼쪽, 오른쪽 ,위, 아래 순서
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x = nx
    y = ny

print(x,y)