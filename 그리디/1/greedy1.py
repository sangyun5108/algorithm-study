n = int(input())
coin_count = 0
money = [500,100,50,10]

for coin in money:
    coin_count+= n//coin
    n = n%coin

print("최소 동전 갯수",coin_count)
