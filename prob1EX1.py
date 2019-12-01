# -*- coding: utf-8 -*-

'''
#### problem 1-1. finding minimum ####

Input:
  target change n
  denomination D = [d1,...,dj]

Temporary lists:
  M[n], denotes a minimum number of coins to make change of n SE380 cents.
  R[n], denotes a way to make change of n SE380 cents, using M[n] number of cents.

Output:
  Output shoud be a list, with following components.
  [number_of_necessary_coins, coin1_num, coin2_num, ... , coinj_num] 리스트, 전체 코인의 숫자와 코인의 개수 별 종류
'''


def minchange_student(n, D):
    # initialize list.
    M = [0 for i in range(n + 1)]
    R = [[0 for col in range(len(D))] for row in range(n + 1)]
    # previous provided code
    K = [[0 for i in range(n + 1)] for i in range(len(D))]

    '''
    코드 설명을 위해 n = 11, D = [1, 5, 6, 8] 로 가정하고 각 코드가 끝날 때마다 리스트 K의 상태를 업데이트하겠습니다.
    K = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    K는 list of list 형태로 열의 개수는 코인의 종류이며 행의 개수는 n+1개입니다.
    K[i][j]는 j 원일때 코인의 종류가 D[:i+1]까지 있다고 가정하고 최소한의 코인으로 지불할 수 있는 코인의 수입니다.
    ex) K[1][10] = 10원일때 1원짜리와 5원짜리로 10원을 최소한의 코인으로 지불하는데 필요한 코인의 수
    '''
    print(K)
    for i in range(0, n+1):
        K[0][i] = i

    '''
        K = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        K의 첫번째 열은 1원짜리 코인으로 n원까지 지불하는데 필요한 코인의 수입니다    
    '''
    for i in range(1,len(D)):
        for j in range(0, n+1):
            if (j == D[i]) or (j > D[i]): # case 1
                K[i][j] = min(K[i-1][j], K[i][j-D[i]]+1)
            else: # case 2
                K[i][j] = K[i-1][j]
    '''
    K = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    K[1]을 예시로 1원과 5원짜리밖에 없는데 n원을 지불해야 한다고 가정하면,
    우선 1~4원을 지불할 때, 즉 case 2에 해당할 때, 5원짜로는 1~4원을 지불할 수 없으므로 K[0][j] 방법대로 지불해야합니다.
    고로
    K = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 
        [0, 1, 2, 3, 4, min(0+1, 5), 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    그러나 5원 이상을 지불할 때, 즉 case 1에 해당할 때 n원 금액을 두 가지 방법으로 지불할 수 있습니다
     i) 5원짜리로 지불하는 방법 ( K[1][j-5] 의 코인에서 5원 하나를 지불하니 +1개를 더함 )
     ii) 1원짜리로 지불하는 방법 ( K[0][j] 개수의 코인으로 지불할 수 있음)
    i과 ii의 방법 중 더 작은 코인으로 지불할 수 있는 방법을 선택해야합니다.
    min(0+1, 5)
    0+1은 K[1][0]의 수에 5원 코인 1개를 더한 수치이고
    5는 1원짜리 다섯개로 지불하는 수치입니다.
    따라서 min(K[i-1][j], K[i][j-D[i]]+1)
    
    이와 같은 방식으로 마지막 코인의 열까지 전부 채워주면 마지막 행 마지막 열이 가장 해당 액수를 지불하는 가장 최소 코인의 수가 됩니다
    '''
    return K[-1][-1]

'''
#### problem 1-2. finding number of distinctive ways. ####

Input:
  target change n
  denomination D= [d1,...,dj]

Temporary lists:
  N[m][n], denotes a number of distinctive ways to make change of n SE380 cents with m kind of denominations.

Output: 얼마나 다양한 방법으로 지불할 수 있는가
  an integer value which denotes a number of distinctive ways to make change of n SE380 cents.
'''


def numways_student(n, D):
    N = [[0 for col in range(n + 1)] for row in range(len(D) + 1)]

    for i in range(len(D)+1):
        N[i][0] = 1
    '''
    코드의 설명을 위해 n = 10, D = [1, 4, 7] 로 가정하고 N의 상태를 업데이트하겠습니다
    N =
    [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    '''

    for i in range(len(D)):
        for j in range(1, n+1):
            if (j > D[i]) or (j == D[i]): # case 1
                N[i][j] = N[i-1][j]+N[i][j-D[i]]
            else: # case 2
                N[i][j] = N[i-1][j]
    print(N)
    return N[len(D)-1][n]

print(numways_student(10, [1, 4, 7]))

#print(minchange_student(11, [1,5,6,8]))
