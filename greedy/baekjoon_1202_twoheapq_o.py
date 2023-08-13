""" 1202 greedy problem - https://www.acmicpc.net/problem/1202 """
import sys
import heapq


def main():
    """main function"""
    # input O(N+K)
    # N, K = map(int, input().split())  # list(map(int, input().split()))
    num_jews, num_bags = map(int, sys.stdin.readline().split())
    jews = []
    weight_of_bag = []
    total_cost_of_jews = 0
    # N * LOG N
    # for _ in range(N):
    #    weight, cost = map(int, input().split())
    #    heapq.heappush(jews, [weight, cost])
    for _ in range(num_jews):
        heapq.heappush(jews, list(map(int, sys.stdin.readline().split())))

    for _ in range(num_bags):
        # weight_of_bag.append(int(input()))
        weight_of_bag.append(int(sys.stdin.readline()))

    # 제일 작은 가방 순
    # O(K LOG K)
    weight_of_bag.sort()

    sorted_possible_jew = []
    min_index = 0
    for bag in weight_of_bag:
        for _ in range(len(jews)):
            if bag >= jews[0][0]:
                heapq.heappush(sorted_possible_jew, -heapq.heappop(jews)[1])
            else:
                break

        if sorted_possible_jew:
            total_cost_of_jews -= heapq.heappop(sorted_possible_jew)

        if not sorted_possible_jew and min_index == num_jews:
            break

    # output
    print(total_cost_of_jews)


if __name__ == "__main__":
    main()
