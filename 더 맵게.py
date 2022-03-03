
#두번째 시도

def solution(scoville, K):
    answer = 0
    scoville.sort()
    new_scoville = scoville[1]
    start_scoville = scoville[0]
    if start_scoville < K:  # 제일 안매운 음식이 애초에 K보다 클 경우 pass
        new_scoville = start_scoville + new_scoville * 2
        for i in range(2, len(scoville)):
            answer += 1
            print(scoville[i], new_scoville)
            if new_scoville >= K and scoville[i] >= K:
                break
            new_scoville = scoville[i] + new_scoville * 2

    if new_scoville < K:  # 모든 음식 섞어도 K이상 불가
        answer = -1
    print(answer)
    return answer


solution(scoville=[0,1, 2, 3, 9, 10, 12, 13,
         15, 18, 18, 37, 189, 1237], K=3)


'''첫번째 시도

def solution(scoville, K):
    answer = 0
    new_scoville = scoville[1]
    for i in range(0, len(scoville), 2):
        answer += 1
        new_scoville = scoville[i] + new_scoville * 2
        print(new_scoville)
        if new_scoville >= K:
            break

    return answer
'''
