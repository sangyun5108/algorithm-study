# 문제 - 거스름돈 

당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하여라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.


### 구현 알고리즘 

```python
  n = int(input())
  coin_count = 0
  money = [500,100,50,10]
  
  for i in range(len(money)):
    coin_count+=n//money[i]
    n = n%money[i]
    
  print(coin_count)
```

```python

  1260 //입력
  최소 동전 갯수 6 //출력 
```

### 이렇게 풀이한 이유

- 최소 동전 갯수를 주어야 하므로, 액수가 큰 금액에서 작은 금액 순으로 거슬러 주었다.


### 책에 나온 알고리즘

```python
  n = int(input())
  coin_count = 0
  money = [500,100,50,10]
  
  for coin in money:
    coin_count += n//coin
    n = n%coin
  
  print(coin_count)
```

- for문을 이용하여 인덱스 값을 통해 배열의 갑을 추출하는 것이아닌, 바로 값을 이용해준다. 
