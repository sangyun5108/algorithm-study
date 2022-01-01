m,n = map(int,input().split())
small_big = 0

for i in range(m):
    lists = list(map(int,input().split()))
    small = min(lists)
    small_big = max(small_big,small)
    

print(small_big)