n, price = map(int, input().split()) # 동전 종류 수, 제시 가격
money, cnt = [int(input()) for x in range(n)], 0 # 동전 종류 리스트, 최소 동전 수
for i in reversed(range(len(money))): # 큰 돈부터 줄 수 있는지 검사
    if price // money[i] != 0:
        cnt += (price // money[i]) # 몇개 줄 수 있는지
        price -= money[i] * (price // money[i]) # 나머지 돈
print(cnt) # 결과 출력
