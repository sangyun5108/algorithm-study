# 문제 - 게임 개발

NxM 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.
맵의 각 칸은 (A,B)로 나타낼 수 있고, A는 북쪽으로부터 멀리 떨어진 칸의 개수, B는 서쪽으로부터 멀리 떨어진 칸의 갯수, 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어있는 공간에는 갈 수 없다.
캐릭터의 움직임을 설정하기 위해 정해놓은 메뉴얼은 이러하다.

- 현재 위치에서 현재 방향을 기준으로 왼쪽방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
- 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.왼족 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
- 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을
멈춘다.


### 구현 알고리즘 
```python
  n,m = map(int,input().split())
  
  #캐릭터가 지나간 위치
  d = [[0]*m for _ in range(n)]
  
  x,y,direction = map(int,input().split())
  
  #캐릭터 현재 위치
  d[x][y] = 1
  
  array = []
  
  # 맵(지형 지물)
  for i in range(n):
    array.append(list(map(int,input().split())))
  
  count = 1
  turn_time = 0
  
  def turn_left:
    global direction
    direction-=1
    if direction == -1
      direction = 3
  
  
  while(True):
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if array[nx][ny]==0 and d[nx][ny]==0:
      x = nx
      y = ny
      count+=1
      turn_time = 0
      continue
    else:
      turn_time+=1
      turn_left()
      
      if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
          x = nx
          y = ny
        else:
          break
        turn_time = 0
print(count)
```

### 이렇게 풀이한 이유 
- 현재 위치에서 현재 방향을 기준으로 왼쪽으로 돌기위해 turn_left()함수 구현
- dx, dy도 인덱스에 맞게 북 -> 동 -> 남 -> 서 방향으로 움직이도록 구현
- turn_left를 하는 경우 현재 방향 direction에서 1씩 빼주면 왼쪽으로 90도 회전이 구현된다.
- 캐릭터가 맵에 이미 도착해본 지역을 구분하기위해 d라는 2차원 배열을 만들어 주었다.
- 지형지물은 값을 받아오기 위해 array라는 변수를 사용해 주었다.
- 이제 게임 시작시 왼쪽으로 돌고(turn_left) 돌고 난 방향에서 한칸 전진한 값 nx,ny가 가보지 않은 칸 이고 지형이 땅으로 되어있다면 x=nx,y=ny로 캐릭터를 1칸이동해준다.
- 만약, 위에 나온 이외의 경우일땐, turn_left 돌고, 돈 횟수를 1개 더해준다. -> 한바퀴 다돌동안 움직일 곳이 없는 경우, 뒤로 가거나 게임을 종료해주어야 하므로 turn_time 변수 사용
- 한바퀴 다 돈 경우(turn_time == 4) 바라보는 방향에서 뒤로가기 nx = x - dx[direction] ny = y - dy[direction]를 해주고, 지형이 바다인지 육지인지 판단해서 육지인 경우 뒤로가주고, turn_time = 0으로 초기화해준다.
- 만약 육지가 아닌 바다인 경우 break로 게임을 종료해준다.



