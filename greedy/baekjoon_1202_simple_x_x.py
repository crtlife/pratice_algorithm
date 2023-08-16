""" 1202 greedy problem - https://www.acmicpc.net/problem/1202 """


def main():
    """main function"""
    # input O(N+K)
    num_jews, num_bags = map(int, input().split())  # list(map(int, input().split()))
    jews = []
    weight_of_bag = []
    total_cost_of_jews = 0
    for _ in range(num_jews):
        weight, cost = map(int, input().split())
        jews.append((cost, weight))

    for _ in range(num_bags):
        weight_of_bag.append(int(input()))

    # logic : 최대한 비싼 보석을 가능한 제일 작은 가방에 넣는다.

    # 비싼 보석 순
    # O(N LOG N)
    jews.sort(key=lambda x: x[0], reverse=True)

    # 제일 작은 가방 순
    # O(K LOG K)
    weight_of_bag.sort()
    # O(N * K)
    for jew in jews:
        jew_cost = jew[0]
        jew_weight = jew[1]

        for i in range(num_bags):
            if weight_of_bag[i] >= jew_weight:
                # list del O(N)
                # del weight_of_bag[i]
                weight_of_bag[i] = 0
                total_cost_of_jews += jew_cost
                break

    # output
    print(total_cost_of_jews)


if __name__ == "__main__":
    main()
