# def dfs(x, y,cnt,n,v):
#     cnt += 1
#     if x <= -1 or x >= n or y <= -1 or y >= n:
#         return False
#
    # if v[x][y] == 0:
    #     v[x][y] = cnt
    #     dfs(x, y + 1,cnt,n,v)
    #     if v[x][y+1] == 0:
    #         dfs(x, y + 1,cnt,n,v)
    #     dfs(x + 1, y,cnt,n,v)
    #     if v[x+1][y] == 0:
    #         dfs(x + 1, y,cnt,n,v)
    #     dfs(x, y - 1,cnt,n,v)
    #     if v[x][y-1] == 0:
    #         dfs(x, y - 1,cnt,n,v)
    #     dfs(x - 1, y,cnt,n,v)
    #     if v[x-1][y] == 0:
    #         dfs(x - 1, y,cnt,n,v)

def can_go(x,y,v,n):
    if x > -1 and x < n and y > -1 and  y < n and v[x][y] == 0:
        return True


def dfs(x, y,cnt,n,v,_x,_y):
    cnt += 1
    # print(cnt)
        # if 온방향 / 앞으로 가고자 하는 방향  => v[x+nx][y+ny] == 0:
    # print(x,y)
    v[x][y] = cnt
    if _x>0 or _y>0:
        # print(nx,ny)
        print(x,y)
        if can_go(x+_x, y+_y, v, n):
            dfs(x+_x, y+_y, cnt, n, v, x, y)
    else:
        # v[x][y] = cnt
        if can_go(x, y+1, v, n):
            dfs(x, y+1, cnt, n, v, 0, 1)
        if can_go(x+1, y, v, n):
            dfs(x+1, y, cnt, n, v, 1, 0)
        if can_go(x, y-1, v, n):
            dfs(x, y-1, cnt, n, v, 0, -1)
        if can_go(x-1, y, v, n):
            dfs(x-1, y, cnt, n, v, -1, 0)

def __main__():
    T = int(input())
    for i in range(1, T+1):
        print('#%d'%i)
        n = int(input())
        v = []
        for j in range(n): # n*n 행렬 만들기
            v.append(list(map(lambda x: 0, range(n))))
        _x,_y,cnt = 0,0,0
        dfs(0,0,cnt,n,v,_x,_y)
        # print(v)
        for p in range(len(v)):
            for q in range(len(v[p])):
                print(v[p][q],end=' ')
            print(sep='\n')
__main__()





# def can_go(x,y,v,n):
#     if x > -1 and x < n and y > -1 and  y < n and v[x][y] == 0:
#         return True
#
#
# def dfs(x, y,cnt,n,v,_x,_y):
#     cnt += 1
#     nx = x-_x
#     ny = y-_y
#     # print(cnt)
#         # if 온방향 / 앞으로 가고자 하는 방향  => v[x+nx][y+ny] == 0:
#     # print(x,y)
#     v[x][y] = cnt
#     if nx>0 or ny>0:
#         # print(nx,ny)
#         print(x,y)
#         if can_go(x+nx, y+ny, v, n):
#             dfs(x+nx, y+ny, cnt, n, v, x, y)
#     else:
#         # v[x][y] = cnt
#         if can_go(x, y+1, v, n):
#             dfs(x, y+1, cnt, n, v, x, y)
#         if can_go(x+1, y, v, n):
#             dfs(x+1, y, cnt, n, v, x, y)
#         if can_go(x, y-1, v, n):
#             dfs(x, y-1, cnt, n, v, x, y)
#         if can_go(x-1, y, v, n):
#             dfs(x-1, y, cnt, n, v, x, y)
#
# def __main__():
#     T = int(input())
#     for i in range(1, T+1):
#         print('#%d'%i)
#         n = int(input())
#         v = []
#         for j in range(n): # n*n 행렬 만들기
#             v.append(list(map(lambda x: 0, range(n))))
#         _x,_y,cnt = 0,0,0
#         dfs(0,0,cnt,n,v,_x,_y)
#         # print(v)
#         for p in range(len(v)):
#             for q in range(len(v[p])):
#                 print(v[p][q],end=' ')
#             print(sep='\n')
# __main__()




















# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
# list(map(lambda x: x ** 2, range(5)))

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
    # # a[0] = list(map(lambda x: x + 1, range(n)))
    #
    # # x는 가로 y는 세로
    # x_line = 0
    # y_line = -1
    # cnt = 0
    # res = 0
    # # _x_line = n
    # # _y_line = n
    # while True:
    #     if res < m**2:
    #         for x in range(n):
    #             a[x_line][x+cnt] = res + 1
    #             res = a[x_line][x+cnt]
    #
    #         for y in range(n-1):
    #             a[y+1][y_line-cnt] = res + 1
    #             res = a[y+1][y_line-cnt]
    #
    #         if res == m**2:
    #             break
    #
    #         for _x in range(n-1,x_line,-1):
    #             a[n-1][_x-cnt-1] = res + 1
    #             res = a[n-1][_x-cnt-1]
    #
    #         for _y in range(n-1,x_line+1,-1):
    #             a[_y+cnt-1][x_line] = res + 1
    #             res = a[_y+cnt-1][x_line]

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














# # graph = []
# # for i in range(n):
# #     graph.append(list(map(int, input())))
# # list(map(lambda x: x ** 2, range(5)))
#
# T = int(input())
# for i in range(1, T+1):
#     print('#%d'%i)
#     n = int(input())
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
#     # _x_line = n
#     # _y_line = n
#     while True:
#         for x in range(n):
#             a[x_line][x+cnt] = a[x_line][(x+cnt)-1] + 1
#
#         for y in range(n-1):
#             a[y+1][y_line-cnt] = a[y][y_line-cnt] + 1
#
#         for _x in range(n-1,x_line,-1):
#             a[n-1][_x-cnt-1] = a[n-1][_x-cnt] + 1
#
#         for _y in range(n-1,x_line+1,-1):
#             a[_y+cnt-1][x_line] = a[_y+cnt][x_line]+1
#
#         x_line += 1
#         y_line += 1
#         cnt += 1
#         # _x_line -= 1
#         # _y_line -= 1
#         n -= 1
#         print(a)
#         if 0 not in a:
#             break
#
#         # a[n-1][x] = a[n-1][x] + 1
#         # print(a[max_num])
#     # print(a)
#
#     for p in range(len(a)):
#         for q in range(len(a[p])):
#             print(a[p][q],end=' ')
#         print(sep='\n')











# size = ['a','b','c','d','e','f','g','h','i','j']
# T = int(input())
# int = map(func, iter1)
# for i in range(1, T+1):
#     print('#%d'%i)
#     n = int(input())
#     a+'i'.format(i) = [0*i]
#     a2 = []
#     for j in range(n):
#         =
#
#     for x in range(len(num_list)):
#         for y in range(len(num_list[x])):
#             print(num_list[x][y],end=' ')
#         print(sep='\n')
