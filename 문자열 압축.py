#
# def solution(s):
#     answer = 0
#     if s[0] not in s[1:]:
#         return print(len(s))
#
#     for i in range(len(s)):
#         if
#
#     return answer
#
#
# solution("xababcdcdababcdcd")

from collections import deque


def solution(progresses, speeds):
    queue = deque([])
    # 한 번에 배포하는 기능의 개수 저장
    distributions = list()
    for progress, speed in zip(progresses, speeds):
        time = (100 - progress) // speed + int((100 - progress) % speed != 0)
        if queue and queue[0] < time:
            # 현재 개발 중인 기능의 개수
            n = len(queue)
            queue.clear()
            distributions.append(n)
        queue.append(time)
        print(queue[0], time)

    # 개발 중인 기능 처리해서 distributions 에 반영
    while queue:
        distributions.append(len(queue))
        queue.clear()

    return print(distributions)


# if __name__ == '__main__':
#     assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
solution([93, 30, 55], [1, 30, 5])
