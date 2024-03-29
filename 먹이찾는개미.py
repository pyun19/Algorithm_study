
# 개미집 미로 크기 선언
miro = [list(map(int, input().split())) for x in range(10)]
x, y = 1, 1  # 시작 좌표
while miro[x][y] != 2:  # 먹이(2)를 찾으면 종료
    miro[x][y] = 9  # 이동한 위치 9로 변환
    if miro[x][y+1] != 1:
        y += 1
    elif miro[x+1][y] != 1:
        x += 1
    else:   # 더이상 갈 곳 없을 때
        break
miro[x][y] = 9  # 마지막 위치 9 변환
for result in miro:  # 결과 출력
    print(*result)
