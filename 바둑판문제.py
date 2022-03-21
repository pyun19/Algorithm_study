# num = int(input())
# back_grd = [[0 for j in range(19)] for i in range(19)]
# for i in range(num):
#     a, b = map(int, input().split())
#     back_grd[a-1][b-1] = 1
# for result in back_grd:
#     print(*result)


back_grd = [list(map(int, input().split())) for x in range(19)]
for i in range(int(input())):
    a, b = map(int, input().split())
    for j in range(19):
        if back_grd[j][b-1] == 0:
            back_grd[j][b-1] = 1
        else:
            back_grd[j][b-1] = 0
        if back_grd[a-1][j] == 0:
            back_grd[a-1][j] = 1
        else:
            back_grd[a-1][j] = 0
for result in back_grd:
    print(*result)
