# n = input()

# #상, 하
# dy = [-1,1]
# #좌, 우
# dx = [1,-1]

# count = 0

# column = int(n[1])
# row = n[0]

# #소문자 a 97나온다.
# row = ord(n[0])-96

# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             if(i==1):
#                 nx = row+2*dx[j]
#                 ny = column+dy[k]
#             else:
#                 nx = row+dx[j]
#                 ny = column+2*dy[k]
            
#             if nx<1 or nx>8 or ny<1 or ny>8:
#                 continue
#             print("nx:{0} ny:{1}".format(nx,ny))
#             count+=1

# print(count)


#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column+step[1]
    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result+=1

print(result)