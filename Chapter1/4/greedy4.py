import time
# start = time.time()

# n,k = map(int,input().split())
# count = 0
# while(True):

#     if(n!=1):
#         if n%k == 0:
#             n//=k
#             count+=1
#         else:
#             n-=1
#             count+=1
#     else:
#         break

# print(count)

# print("time:",time.time()-start)

start = time.time()

n, k = map(int,input().split())
result = 0

while True:
    # 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k)*k
    result += (n-target)
    n = target

    #n<k보다 작은경우-> 더이상 나눌 수 없는 경우
    if n<k:
        break
    
    result+=1
    n//=k

# 남은 수에 대해서 1씩 빼기
result += (n-1)
print(result)

print("time:",time.time()-start)