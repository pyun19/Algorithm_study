h, w = map(int, input().split())  # 세로 * 가로
back_grd = [[0 for y in range(w)] for x in range(h)]  # 게임판 선언
for i in range(int(input())):
    l, d, x, y = map(int, input().split())  # 막대 길이, 방향(가로:0, 세로:1), 좌표 x, 좌표 y
    x, y = x-1, y-1
    if d == 0:
        for j in range(l):
            back_grd[x][y+j] = 1
    else:
        for j in range(l):
            back_grd[x+j][y] = 1
for result in back_grd:
    print(*result)
