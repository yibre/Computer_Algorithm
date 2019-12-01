import argparse
import pickle as pk

tables_ex = {'A': [-1, 339, 165, 0, 35, 59, 203, 785, 867, 225, 905],
             'B': [-1, 9, 818, 510, 400, 997, 341, 549, 412, 294, 185]}

# print(tables_ex['A'][1])
# output format = list, [n날의 fish 의 수, char type n날 A 호수인지 B 호수인지]
# ex) [int, 'A'], [int, 'B']

count = [0]
def DP_Fish(tables, L, n):
    count[0] = count[0]+1
    fishA = tables['A'][n]
    #print(len(tables['A'])) = 100
    fishB = tables['B'][n]

    if (n == 0):
        return [0, 'A']

    fishBefore = DP_Fish(tables, L, n - 1)[0]
    lakeBefore = DP_Fish(tables, L, n - 1)[1]

    if (abs(fishA - fishB) > L):  # ex: tax = 5, (A,B) = (1, 9), (2, 8)
        # tax를 지불하는게 그대로 남아있는 것보다 크면 이동해야함
        if (fishA > fishB):
            return [[fishBefore + fishA - L][0], 'A']
        else:
            return [[fishBefore + fishB - L][1], 'B']
    else:  # ex: tax = 5, (A, B) = (2, 3), (4, 7)
        # 현행 상태 유지
        if (lakeBefore == 'A'):
            return [[fishBefore + fishA][0], 'A']
        elif (lakeBefore == 'B'):
            return [[fishBefore + fishB][0], 'B']
        else:
            print("Error report")
            pass  # error report


if __name__ == "__main__":
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
    # 수정함, 리스트 형식으로 output을 고침

    print("L : [{:d}] n : [{:d}] result : [{:d}]".format(L, n, result))
    print(count[0])