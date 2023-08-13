""" 2839 greedy problem - https://www.acmicpc.net/problem/5585 """


def main():
    """main function"""
    # input
    number = int(input())
    kind_of_change = [500, 100, 50, 10, 5, 1]
    change = 1000 - number
    count_of_coin = 0
    for kind in kind_of_change:
        count_of_coin = count_of_coin + change // kind
        change = change % kind
    #        print("kind: ", kind, ", change: ", change, ",count_of_coin:", count_of_coin)
    print(count_of_coin)


if __name__ == "__main__":
    main()
