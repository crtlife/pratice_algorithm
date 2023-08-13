""" 1202 greedy problem - https://www.acmicpc.net/problem/1202 """
import sys
import heapq


def read_jews_in_heap_by_weight(num_jews, jews):
    """
    Args:
        num_jews (int): num of jews
        jews (list): heap of jews - ordered by weight of jew
    """
    for _ in range(num_jews):
        heapq.heappush(jews, list(map(int, sys.stdin.readline().split())))


def read_bags(num_bags, weight_of_bag):
    """
    Args:
        num_bags (_type_): num of bags
        weight_of_bag (_type_): list of bags
    """
    for _ in range(num_bags):
        # weight_of_bag.append(int(input()))
        weight_of_bag.append(int(sys.stdin.readline()))


def find_total_cost_of_jews_in_bags(weight_of_bag, num_jews, jews_heap):
    """_summary_
    Args:
        weight_of_bag (_type_): _description_
        num_jews (_type_): _description_
        jews_heap (_type_): _description_

    Returns:
        _type_: total_cost_of_jews
    """
    total_cost_of_jews = 0
    sorted_possible_jew_heap = []
    min_index = 0
    for bag in weight_of_bag:
        for _ in range(len(jews_heap)):
            # 가방 안에 넣을 수 있는 보석을 찾기.
            if bag >= jews_heap[0][0]:
                # 비싼 비용 순으로 heap에 넣기
                heapq.heappush(sorted_possible_jew_heap, -heapq.heappop(jews_heap)[1])
            else:
                break

        if sorted_possible_jew_heap:
            total_cost_of_jews -= heapq.heappop(sorted_possible_jew_heap)

        if not sorted_possible_jew_heap and min_index == num_jews:
            break

    return total_cost_of_jews


def main():
    """main function"""
    # input O(N+K)
    # N, K = map(int, input().split())  # list(map(int, input().split()))
    num_jews, num_bags = map(int, sys.stdin.readline().split())
    jews_heap = []
    weight_of_bag = []

    read_jews_in_heap_by_weight(num_jews, jews_heap)
    read_bags(num_bags, weight_of_bag)

    # 제일 작은 가방 순
    # O(K LOG K)
    weight_of_bag.sort()

    # output
    print(find_total_cost_of_jews_in_bags(weight_of_bag, num_jews, jews_heap))


if __name__ == "__main__":
    main()
