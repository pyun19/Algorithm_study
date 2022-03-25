
h, w = map(int, input().split())  # 세로 * 가로
back_grd = [[0 for y in range(w)] for x in range(h)]  # 게임판 선언
for i in range(int(input())):
    # 막대 길이, 방향(가로:0, 세로:1), 좌표 x, 좌표 y
    l, d, x, y = map(int, input().split())
    # 시작 좌표 0, 0 변환
    x, y = x-1, y-1
    if d == 0:  # 막대가 가로 방향이면
        for j in range(l):  # 막대 크기 l만큼 가로를 1로 변환
            back_grd[x][y+j] = 1
    else:  # 막대가 세로 방향이면
        for j in range(l):  # 막대 크기 l만큼 세로를 1로 변환
            back_grd[x+j][y] = 1
for result in back_grd:  # 결과 출력
    print(*result)
