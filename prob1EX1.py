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

    


    return 0

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
    # initialize list.
    N = [[0 for col in range(n + 1)] for row in range(len(D) + 1)]
    # your code goes in here.#

    for i in range(len(D)+1):
        N[i][0] = 1

    for i in range(len(D)):
        for j in range(1, n+1):
            if (j > D[i]) or (j == D[i]):
                N[i][j] = N[i-1][j]+N[i][j-D[i]]
            else:
                N[i][j] = N[i-1][j]
    print(N)
    return N[len(D)-1][n]
''' n = 10 # 줘야하는 액수
    D = [1, 4, 7] # 코인의 종류
    
    백준 코드: n = 코인 종류의 개수 k = 전체 액수
    coins = 우리 코드에서의 D와 같음
    d[0] = 1
'''


print(numways_student(10, [1, 4, 7]))