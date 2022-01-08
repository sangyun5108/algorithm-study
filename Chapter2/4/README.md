# 문제 - 문자열 재정렬

알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력한다.


### 구현 알고리즘

```python
  n = input()
  
  alphabet = []
  number_sum = 0
  
  for step in n:
      if(ord(step)>=65):
          alphabet.append(step)
      else:
          number_sum+=int(step)
          
  alphabet.sort()
  alphabet.append(str(number_sum))
  
  
  for answer in alphabet:
      print(answer,end='')
```

### 이렇게 풀이한 이유

- ASCII 코드 변환을 통해 알파벳과 숫자를 분리하는 기준을 가졌다.
- 알파벳일 경우, alphabet이라는 배열에 append해주고, 숫자인 경우 number_sum에 숫자를 더해주었다.

### 책에 구현된 알고리즘

```python
   # 문자를 하나씩 확인하며
   for x in data:
      # 알파벳인 경우 결과 리스트에 삽입
      if x.isalpha():
        result.append(x)
      #숫자는 따로 더해주기
      else:
        value += int(x)
   # 알파벳을 오름차순으로 정렬
   result.sort()
   
   # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
   if value!=0:
        result.append(str(value))
        
   # 최종 결과 출력(리스트를 문자열로 변환하여 출력)
   
   print(''.join(result))
```

### 새로 알게된 내장함수
- isalpha() : 현재 값이 앒파벳인지 아닌지 확인해준다.
- join() : 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 변환해준다.
- 사용법 1 : ".join(리스트)를 이용하면 매개변수로 들어온 ['a','b','c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해준다.
- 사용법 2 : '구분자.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문장열로 합쳐준다.
'_'.join(['a','b','c'])라 하면 "a_b_c"와 같은 형태로 만들어준다.

