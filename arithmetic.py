def add(list_o_nums):
    answer = 0
    for num in list_o_nums:
        answer += num
    return answer


def subtract(list_o_nums):
    answer = list_o_nums[0]
    for num in list_o_nums[1:]:
        answer -= num
    return answer


def multiply(list_o_nums):
    answer = 1
    for num in list_o_nums:
        answer *= num
    return answer


def divide(list_o_nums):
    # Need to turn at least argument to float for division to
    # not be integer division
    answer = float(list_o_nums[0])
    for num in list_o_nums[1:]:
        answer /= float(num)
    return answer


def square(list_o_nums):
    # Needs only one argument
    answer = []
    for num in list_o_nums:
        answer.append(num**2)
    return answer


def cube(list_o_nums):
    # Needs only one argument
    answer = []
    for num in list_o_nums:
        answer.append(num**3)
    return answer


def power(list_o_nums):
    answer = list_o_nums[0]
    for num in list_o_nums[1:]:
        answer = answer ** num
    return answer


def mod(list_o_nums):
    answer = list_o_nums[0]
    for num in list_o_nums[1:]:
        answer = answer % num
    return answer
