n,m,k = map(int,input().split())
number_list = list(map(int,input().split()))
number_list.sort(reverse=True)

# result = 0
# count_three = 0
# i = 0

# while(m!=0):
#     if(count_three==k):
#         result+=number_list[i+1]
#         count_three = 0
#     else:
#         result+=number_list[i]
#         count_three+=1
#     m-=1

# print(result)

first = number_list[0]
second = number_list[1]
big_count = m//(k+1)*k + m%(k+1)*k

result = first*big_count + (m-big_count)*second

print(result)
