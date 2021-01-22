

a=int(input())
for j in range(a):
    n=''
    for z in str(j+1):
        if z=='3' or z=='6' or z=='9':
            z = '-'
        n += ''.join(z)
        if n.count('-')==1:
            n='-'
    print(n,end=' ')


###################2번째 시도
# T = int(input())
# for i in range(1, T+1):
#     a = int(input())
#     res = []
#     for j in range(a):
#         num = str(j+1)
#         fin = ''
#         for z in num:
#             if z == '3' or z == '6' or z == '9':
#                 z = '-'
#             fin += ''.join(z)
#             if '-' in fin:
#                 fin = '-'
#         res.append(fin)
#     for x in range(len(res)):
#         print(res[x],end=' ')



###################1번째 시도
# T = int(input())
# for i in range(1, T+1):
#     a = int(input())
#     res = []
#     num = []
#     for j in range(a):
#         num.append(str(j+1))
#         res_s = []
#         for z in num[j]:
#             if z == '3' or z == '6' or z == '9':
#                 z = '-'
#             res_s.append(z)
#             fin = ''.join(res_s)
#         res.append(fin)
#     for x in range(len(res)):
#         print(res[x],end=' ')
