# 문제 - 모험가

한 마을에 모험가 N명이 있다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데, '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로
대처할 능력이 떨어진다. 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모함가 그룹에 참여해야 여행을
떠날 수 있도록 규정했다. 동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금하다. N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을
구하는 프로그램을 작성하라.

### 구현 알고리즘

```python
  n = int(input())
  
  fear = list(map(int,input().split()))
  
  fear.sort()
  
  current_user = 0
  result = 0
  
  for i in range(0,len(fear)):
      current_user+=1
      if(fear[i]<=current_user):
          result+=1
          current_user = 0
  print(result)
```

### 이렇게 풀이한 이유

- 공포도 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야하 하므로, 공포도를 오름차순 정렬해서 제일 낮은 사람부터 그룹을 짝지어주었다.
- for문을 이용해서 현재 인원과 공포도를 비교해 현재인원이 더 많거나 같은 경우 하나의 그룹으로 묶어주었다.

### 책에나온 알고리즘

```python
  for i in fear:
      current_user+=1
      if(i<=current_user):
          result+=1
          current_user = 0
```
- range를 사용하지 않고, for in을 이용해 주었다.
