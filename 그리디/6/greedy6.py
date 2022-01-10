n = int(input())

fear = list(map(int,input().split()))

fear.sort()

current_user = 0

result = 0

for i in fear:
    current_user+=1
    if(i<=current_user):
        result+=1
        current_user = 0

print(result)