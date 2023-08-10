""" 2839 greedy problem - https://www.acmicpc.net/problem/2839 """
def cal_quotient_of_divide_5 (number) :
    """ Args: number (number)
        Returns: number : quotient_of_divide_5 
    """
    quotient = -1
    remain = number % 5
    if remain != 0 :
        quotient = -1
    else :
        quotient = number // 5
    return quotient

def main():
    """ main function """
    #input
    number = int(input())

    # 입력된 숫자가 3의 배수로 구성될 수 있는 모든 경우의 수 (3의 배수가 0개 ~ number //3개까지)
    number_of_3 = number // 3 + 1
    result = -1
    # 3의 배수의 개수를 1개씩 늘려서 5를 최대화할 수 있는 숫자 찾기
    for i in range(number_of_3) :
        candidate_of_divide_5 = number - 3*i
        if candidate_of_divide_5 == 0 :
            result = i
            break
        result_divide_5 = cal_quotient_of_divide_5(candidate_of_divide_5)
        if result_divide_5 != -1 :
            result = result_divide_5 + i
            break
    #output
    print(result)

if __name__ == '__main__':
    main()