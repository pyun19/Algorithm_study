
#
# num = int(input())  # 흰 돌 개수
# back_grd = [[0 for j in range(19)] for i in range(19)]  # 바둑판 크기 19 * 19
# for i in range(num):  # 흰 돌을 좌표로 넣자
#     a, b = map(int, input().split())
#     back_grd[a-1][b-1] = 1  # 흰 돌 올려지면 1
# for result in back_grd:
#     print(*result)  # 결과 출력


# 바둑알이 깔려 있는 입력값 받기
back_grd = [list(map(int, input().split())) for x in range(19)]
for i in range(int(input())):  # 십자 뒤집기 횟수
    x, y = map(int, input().split())  # 십자 뒤집기 좌표
    for j in range(19):  # 좌표에 따른 뒤집기 실행
        # if back_grd[j][y-1] == 0:  # 세로줄 뒤집기 0이면 1로 or 1이면 0으로
        #     back_grd[j][y-1] = 1
        # else:
        #     back_grd[j][y-1] = 0
        if back_grd[x-1][j] == 0:  # 가로줄 뒤집기 0이면 1로 or 1이면 0으로
            back_grd[x-1][j] = 1
        else:
            back_grd[x-1][j] = 0
for result in back_grd:  # 결과 출력
    print(*result)
