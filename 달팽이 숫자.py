#
# T = int(input())
# for i in range(1, T+1):
#     print('#%d'%i)
#     n = int(input())
#     m = n
#     a = []
#     for j in range(n): # n*n 행렬 만들기
#         a.append(list(map(lambda x: 0, range(n))))
#
#     # for x in range(n**2):
#     # while 0 not in a:
#
#     # a[0] = list(map(lambda x: x + 1, range(n)))
#
#     # x는 가로 y는 세로
#     x_line = 0
#     y_line = -1
#     cnt = 0
#     res = 0
#     # _x_line = n
#     # _y_line = n
#     while True:
#         if res < m**2:
#             for x in range(n):
#                 a[x_line][x+cnt] = res + 1
#                 res = a[x_line][x+cnt]
#
#             for y in range(n-1):
#                 a[y+1][y_line-cnt] = res + 1
#                 res = a[y+1][y_line-cnt]
#
#             if res == m**2:
#                 break
#
#             for _x in range(n-1,x_line,-1):
#                 a[n-1][_x-cnt-1] = res + 1
#                 res = a[n-1][_x-cnt-1]
#
#             for _y in range(n-1,x_line+1,-1):
#                 a[_y+cnt-1][x_line] = res + 1
#                 res = a[_y+cnt-1][x_line]
#
#             n -= 1
#             x_line += 1
#             y_line += 1
#             cnt += 1
#
#         else:
#             break
#
#         # if cnt == 1:
#         # _x_line -= 1
#         # _y_line -= 1
#         n -= 1
#         print(a)
#
#         # a[n-1][x] = a[n-1][x] + 1
#         # print(a[max_num])
#     # print(a)
#
#     for p in range(len(a)):
#         for q in range(len(a[p])):
#             print(a[p][q],end=' ')
#         print(sep='\n')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # graph = []
# # for i in range(n):
# #     graph.append(list(map(int, input())))
# # list(map(lambda x: x ** 2, range(5)))
#
# # T = int(input())
# # for i in range(1, T+1):
# #     print('#%d'%i)
# #     n = int(input())
# #     m = n
# #     a = []
# #     for j in range(n): # n*n 행렬 만들기
# #         a.append(list(map(lambda x: 0, range(n))))
# #
# #     # for x in range(n**2):
# #     # while 0 not in a:
# #
# #     # a[0] = list(map(lambda x: x + 1, range(n)))
# #
# #     # x는 가로 y는 세로
# #     x_line = 0
# #     y_line = -1
# #     cnt = 0
# #     res = 0
# #     # _x_line = n
# #     # _y_line = n
# #     while True:
# #         if res < m**2:
# #             for x in range(n):
# #                 a[x_line][x+cnt] = res + 1
# #                 res = a[x_line][x+cnt]
# #
# #             for y in range(n-1):
# #                 a[y+1][y_line-cnt] = res + 1
# #                 res = a[y+1][y_line-cnt]
# #
# #             if res == m**2:
# #                 break
# #
# #             for _x in range(n-1,x_line,-1):
# #                 a[n-1][_x-cnt-1] = res + 1
# #                 res = a[n-1][_x-cnt-1]
# #
# #             for _y in range(n-1,x_line+1,-1):
# #                 a[_y+cnt-1][x_line] = res + 1
# #                 res = a[_y+cnt-1][x_line]
# #
# #             n -= 1
# #             x_line += 1
# #             y_line += 1
# #             cnt += 1
# #
# #         else:
# #             break
# #
# #         # if cnt == 1:
# #         # _x_line -= 1
# #         # _y_line -= 1
# #         n -= 1
# #         print(a)
# #
# #         # a[n-1][x] = a[n-1][x] + 1
# #         # print(a[max_num])
# #     # print(a)
# #
# #     for p in range(len(a)):
# #         for q in range(len(a[p])):
# #             print(a[p][q],end=' ')
# #         print(sep='\n')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # # graph = []
# # # for i in range(n):
# # #     graph.append(list(map(int, input())))
# # # list(map(lambda x: x ** 2, range(5)))
# #
# # T = int(input())
# # for i in range(1, T+1):
# #     print('#%d'%i)
# #     n = int(input())
# #     a = []
# #     for j in range(n): # n*n 행렬 만들기
# #         a.append(list(map(lambda x: 0, range(n))))
# #
# #     # for x in range(n**2):
# #     # while 0 not in a:
# #
# #     # a[0] = list(map(lambda x: x + 1, range(n)))
# #
# #     # x는 가로 y는 세로
# #     x_line = 0
# #     y_line = -1
# #     cnt = 0
# #     # _x_line = n
# #     # _y_line = n
# #     while True:
# #         for x in range(n):
# #             a[x_line][x+cnt] = a[x_line][(x+cnt)-1] + 1
# #
# #         for y in range(n-1):
# #             a[y+1][y_line-cnt] = a[y][y_line-cnt] + 1
# #
# #         for _x in range(n-1,x_line,-1):
# #             a[n-1][_x-cnt-1] = a[n-1][_x-cnt] + 1
# #
# #         for _y in range(n-1,x_line+1,-1):
# #             a[_y+cnt-1][x_line] = a[_y+cnt][x_line]+1
# #
# #         x_line += 1
# #         y_line += 1
# #         cnt += 1
# #         # _x_line -= 1
# #         # _y_line -= 1
# #         n -= 1
# #         print(a)
# #         if 0 not in a:
# #             break
# #
# #         # a[n-1][x] = a[n-1][x] + 1
# #         # print(a[max_num])
# #     # print(a)
# #
# #     for p in range(len(a)):
# #         for q in range(len(a[p])):
# #             print(a[p][q],end=' ')
# #         print(sep='\n')
#
#
#
#
#
#
#
#
#
#
#
# # size = ['a','b','c','d','e','f','g','h','i','j']
# # T = int(input())
# # int = map(func, iter1)
# # for i in range(1, T+1):
# #     print('#%d'%i)
# #     n = int(input())
# #     a+'i'.format(i) = [0*i]
# #     a2 = []
# #     for j in range(n):
# #         =
# #
# #     for x in range(len(num_list)):
# #         for y in range(len(num_list[x])):
# #             print(num_list[x][y],end=' ')
# #         print(sep='\n')
