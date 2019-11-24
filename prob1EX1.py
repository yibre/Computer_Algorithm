'''
#### problem 1-1. finding minimum ####

Input:
  target change n
  denomination D = [d1,...,dj] //  코인의 종류가 담긴 list

Temporary lists:
  M[n], denotes a minimum number of coins to make change of n SE380 cents.
  R[n], denotes a way to make change of n SE380 cents, using M[n] number of cents.

Output:
  Output shoud be a list, with following components.
  [number_of_necessary_coins, coin1_num, coin2_num, ... , coinj_num]
'''


def minchange_student(n, D):
    # initialize list.
    M = [0 for i in range(n + 1)]
    R = [[0 for col in range(len(D))] for row in range(n + 1)]

    # your code goes in here.#

    #
    R[0] = sum(R)  # 리스트의 첫번째 원소는 나머지 원소들의 총합과 같다
    return R[n]


'''
#### problem 1-2. finding number of distinctive ways. ####

Input:
  target change n
  denomination D= [d1,...,dj]

Temporary lists:
  N[m][n], denotes a number of distinctive ways to make change of n SE380 cents with m kind of denominations.

Output:
  an integer value which denotes a number of distinctive ways to make change of n SE380 cents.
'''


def numways_student(n, D):
    # initialize list.
    N = [[0 for col in range(n + 1)] for row in range(len(D) + 1)]

    # your code goes in here.#

    return N[len(D)][n]