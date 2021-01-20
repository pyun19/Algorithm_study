#
#
# T = int(input())
# grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
# for i in range(1, T+1):
#     total_std = []
#     search = list(map(int,input().split()))
#     grd_cnt = search[0]//10
#     for j in range(search[0]):
#         score = list(map(int,input().split()))
#         std = score[0]*0.35 + score[1]*0.45 + score[2]*0.2
#         total_std.append(std)
#     z,std_cnt = 0,0
#     while total_std[search[1]-1] != max(total_std):
#         total_std.remove(max(total_std))
#         if std_cnt == grd_cnt:
#             z += 1
#             std_cnt = 0
#         std_cnt += 1
#     if std_cnt == grd_cnt:
#         z += 1
#     print('#%d'%i, grade[z])
#
#     print(total_std)
#     print(std_cnt,grd_cnt)
#
#
#
#
# T = int(input())
# grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
# for i in range(1, T+1):
#     total_std = []
#     search = list(map(int,input().split()))
#     grd_cnt = search[0]//10
#     for j in range(search[0]):
#         score = list(map(int,input().split()))
#         std = score[0]*0.35 + score[1]*0.45 + score[2]*0.2
#         total_std.append(std)
#     z,std_cnt = 0,0
#     while True:
#         total_std.remove(max(total_std))
#         if std_cnt == grd_cnt:
#             z += 1
#             std_cnt = 0
#         std_cnt += 1
#         if total_std[search[1]-1] == max(total_std):
#             if std_cnt == grd_cnt:
#                 z += 1
#             break
#     print('#%d'%i, grade[z])



T = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for i in range(1, T+1):
    total_std = []
    search = list(map(int,input().split()))
    grd_cnt = search[0]//10
    for j in range(search[0]):
        score = list(map(int,input().split()))
        std = score[0]*0.35 + score[1]*0.45 + score[2]*0.2
        total_std.append(std)
    z,std_cnt = 0,0
    while True:
        # if std_cnt == grd_cnt:
        #     z += 1
        if total_std[search[1]-1] != max(total_std):
            idx = total_std.index(max(total_std))
            # print(idx)
            print(total_std[idx])
            total_std[idx] = 0
            # print(std_cnt,grd_cnt)
            if std_cnt == grd_cnt:
                z += 1
                std_cnt = 0
            std_cnt += 1
        else:
            if std_cnt == grd_cnt:
                z += 1
            break
        # print(z,'z값 =========',std_cnt,'cnt값 ======')
    print(total_std)
    print('#%d'%i, grade[z])

    # while total_std[search[1]-1] != max(total_std):
    # print(total_std[search[1]-1],max(total_std),search[1]-1,end='  //')
