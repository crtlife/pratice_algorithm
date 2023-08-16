""" 1202 greedy problem - https://www.acmicpc.net/problem/1202 """
import sys
import heapq


def main():
    """main function"""
    # input O(N+K)
    num_jews, num_bags = map(
        int, sys.stdin.readline().split()
    )  # list(map(int, input().split()))
    jews = []
    weight_of_bag = []
    total_cost_of_jews = 0
    for index in range(num_jews):
        weight, cost = map(int, sys.stdin.readline().split())
        jews.append((cost, weight))

    for _ in range(num_bags):
        weight_of_bag.append(int(sys.stdin.readline()))

    # logic : 최대한 비싼 보석을 가능한 제일 작은 가방에 넣는다.

    # 가벼운 보석 순
    # O(N LOG N)
    jews.sort(key=lambda x: x[1])

    # 제일 작은 가방 순
    # O(K LOG K)
    weight_of_bag.sort()

    sorted_possible_jew = []
    min_index = 0
    for bag in weight_of_bag:
        for index in range(min_index, num_jews):
            if bag >= jews[index][1]:
                heapq.heappush(sorted_possible_jew, -jews[index][0])
                min_index = index + 1
        if sorted_possible_jew:
            total_cost_of_jews -= heapq.heappop(sorted_possible_jew)

        if not sorted_possible_jew and min_index == num_jews:
            break

    # output
    print(total_cost_of_jews)


if __name__ == "__main__":
    main()
