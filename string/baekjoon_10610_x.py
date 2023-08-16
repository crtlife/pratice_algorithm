""" 10610 string - https://www.acmicpc.net/problem/10610 """


def is_multiple_of_30(num_string):
    """
    Args:
        num_string (string): 숫자들로 구성된 문자열
    Returns:
        boolean : multipel of 30 이면 true 아니면 false
    """
    check_result = False
    is_zero_contained = False
    sum_num = 0
    for i in num_string:
        num = int(i)
        if not is_zero_contained and num == 0:
            is_zero_contained = True
        sum_num += num

    if sum_num % 3 == 0 and is_zero_contained:
        check_result = True

    return check_result


def main():
    """main function"""
    num_string = input()

    sorted_num_list = list(num_string)

    result_str = ""
    if is_multiple_of_30(num_string):
        sorted_num_list.sort(reverse=True)
        result_str = "".join(sorted_num_list)
    else:
        result_str = "-1"

    print(result_str)


if __name__ == "__main__":
    main()
