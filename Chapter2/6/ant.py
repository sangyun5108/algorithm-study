
d = []

for i in range(10):
  n = list(map(int,input().split()))
  d.append(n)

x = 1
y = 1
count = 0

while(True):

  count+=1

  d[x][y]=9

  if(d[x][y+1]!=1):
    y+=1
  else:
    x+=1

  if(d[x][y]==2):
    d[x][y]=9
    break

  if(count==15):
    break

      

for i in range(10):
    for j in range(10):
        print(d[i][j],end=' ')
    print()

print()