num = int(input())  # 사람 수
time = sorted(list(map(int, input().split())))  # 시간 짧은 순 정렬
next_time, result = 0, 0  # 누적 시간, 결과 선언
for i in range(num):  # 사람 수 만큼 누적 시간 더하기
    next_time += time[i]
    result += next_time
print(result)  # 결과 출력
