# -*- coding: utf-8 -*-
import argparse
import pickle as pk

tables_ex = {'A': [-1,15, 2, 6],
             'B': [-1, 4, 3, 70]}


# L은 세금 n은 전체 낚시하는 날짜
'''
DP_Fish (tables, L, n) 의 output은 리스트로 [ n번째 날짜인 날 낚는 물고기의 수 && n번째 날짜에 어느 호수에 있는가] 로
구성되어 있다.
[물고기의 수, 레이크 'A' 'B']
ex: [3, 'A'] # A 호수에서 3마리의 물고기를 가지고 있다.
'''
def DP_Fish(tables, L, n):
    if (n == 1):
        return [tables['A'][1], 'A']
    # 만약 첫번째 날이라면, 킴씨는 북극곰에게 세금으로 낼 물고기가 없으므로 무조건 A 에서만 낚을 수 있다.

    elif (n > 1): # 두번째 날부터
        FishBefore = DP_Fish(tables, L, n-1)[0] # n-1번째 날에 낚을 수 있는 물고기의 개수
        lakeBefore = DP_Fish(tables, L, n-1)[1] # n-1번째 날에 킴씨가 존재하는 호수
        FishTodayA = tables['A'][n] # n번째 날에 킴씨가 A 호수에서 낚을 수 있는 물고기 수
        FishTodayB = tables['B'][n] # n번째 날에 킴씨가 B 호수에서 낚을 수 있는 물고기 수

        if FishBefore < L: # 킴씨가 가지고 있는 물고기가 세금을 못 낼 만큼 작다면 킴씨는 존재하던 호수에서 낚아야한다
            if (lakeBefore == 'A'): # 킴씨가 그 전날 A호수에 있었다면 A에서 낚아야 한다
                return [FishBefore + FishTodayA, 'A']
            return [FishBefore + FishTodayB, 'B'] # 킴씨가 전날 B 호수에 있었다면 B에서 낚아야한다.

        if (FishTodayA - FishTodayB > L): # 만약 킴씨가 B호수에 있었는데 A호수에 가는게 세금을 지불하고도 더 이득이라면
            if (lakeBefore == 'A'): # A호수에 남아있었다면 A호수에서 그대로 낚는다.
                return [FishBefore + FishTodayA, 'A']
            else: # B 호수에 있었다면 세금을 지불하고 A호수로 간다
                return [FishBefore + FishTodayA - L, 'A']
        elif (FishTodayB - FishTodayA > L): # 킴씨가 A호수에 있었는데 B호수에 가는게 세금을 지불하고도 더 이득이라면
            if (lakeBefore == 'A'): # A호수에 있었다면 B호수로 간다
                return [FishBefore + FishTodayB - L, 'B']
            else: # B 호수에 있었다면 그대로 B 호수에서 낚는다.
                return [FishBefore + FishTodayB, 'B']
        else: # 만약 세금을 지불하고도 이동하는 것보다 남아있는게 더 이득이라면
            if (lakeBefore == 'A'):
                return [FishBefore + FishTodayA, 'A'] # A호수에 남아있었으면 그대로 A 에 있는다
            return [FishBefore + FishTodayB, 'B'] # B호수에 있으면 그대로 B에 있는다.

    else:
        print("error")
        pass

if __name__ == "__main__":
    print(DP_Fish(tables_ex, 5, 3))

    parser = argparse.ArgumentParser()
    parser.add_argument("--payment", type=int, default=3, help="payment for Polar bear")
    parser.add_argument("--days", type=int, default=10, help="How many days")
    parser.add_argument("--tables", type=str, default='./tables.pk', help="Address of tables.pk")
    opt = parser.parse_args()

    # payment for Polar bear L
    L = opt.payment

    # How many days
    n = opt.days

    # tables of A lake & B lake
    table_path = opt.tables
    f = open(table_path, 'rb')
    tables = pk.load(f)
    f.close()

    result = DP_Fish(tables, L, n)[0]
    # DP_Fish는 리스트 형식이므로 물고기의 수를 알기 위해서는 리스트의 첫 번째 요소를 반환해야한다.

    print("L : [{:d}] n : [{:d}] result : [{:d}]".format(L, n, result))
