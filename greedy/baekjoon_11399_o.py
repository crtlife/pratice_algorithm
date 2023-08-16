""" 11399 greedy problem - https://www.acmicpc.net/problem/11399 """
import sys


def main():
    """main function"""
    # input
    number = int(input())
    withdrawltime_list = list(map(int, sys.stdin.readline().split()))

    if number != len(withdrawltime_list):
        print("Input Length Error!!")

    # 매번 시간이 가장 작은 사람을 뽑아서 인출을 하게 하면 됨
    # 시간이 작은 순으로 정렬
    withdrawltime_list.sort()
    withdrawltime = 0
    total_withdrawltime = 0

    for i in range(number):
        withdrawltime = withdrawltime + withdrawltime_list[i]
        total_withdrawltime += withdrawltime

    print(total_withdrawltime)


if __name__ == "__main__":
    main()
