#
# def solution(id_list, report, k):
#     answer = []
#     _report = [report[x].split() for x in range(len(report))]
#
#     temp = {x: [] for x in id_list}
#     for key, val in _report:
#         # 한명이 동일한 유저에 대한 신고 횟수는 1회 처리
#         if val not in temp[key]:
#             temp.setdefault(key, []).append(val)
#     temp_val = [y for x in temp.values() for y in x]
#     for i in range(len(id_list)):
#         cnt = 0
#         try:
#             for j in temp[id_list[i]]:
#                 if temp_val.count(j) >= k:
#                     cnt += 1
#         finally:
#             answer.append(cnt)
#     print(temp)
#     print(answer)
#
#     return answer

# def solution(id_list, report, k):
#     answer = []
#     report = set(report)
#     _report = [report[x].split() for x in range(len(report))]
#     temp = {x: [] for x in id_list}
#     temp_val = []
#
#     for key, val in _report:
#         if val not in temp[key]:
#             temp.setdefault(key, []).append(val)
#             temp_val.append(val)
#
#     for i in range(len(id_list)):
#         cnt = 0
#         for j in temp[id_list[i]]:
#             if temp_val.count(j) >= k:
#                 cnt += 1
#         answer.append(cnt)
#         print(answer)
#     return answer

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {x: 0 for x in id_list}

    for r in set(report):
        a, b = r.split()
        reported[b] += 1

    for r in set(report):
        a, b = r.split()
        if reported[b] >= k:
            answer[id_list.index(a)] += 1

    print(answer)
    return answer


if __name__ == '__main__':
    assert solution(["muzi", "frodo", "apeach", "neo"], [
                    "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
    assert solution(["con", "ryan"], ["ryan con",
                    "ryan con", "ryan con", "ryan con"], 3)
