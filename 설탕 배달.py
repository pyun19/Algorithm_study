suger = int(input())  # 설탕 무게
cnt = 0  # 봉지 갯수
while suger >= 0:
    if suger % 5 == 0:  # 5로 나누어 떨어질 때 5kg 봉지에 담는다
        cnt += suger // 5
        break
    suger -= 3  # 5로 나눠지지 않으면 3kg 봉지에 담는다
    cnt += 1
else:
    cnt = -1  # 정확하게 N kg을 만들 수 없다면 -1
print(cnt)
