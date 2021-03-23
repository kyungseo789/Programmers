from itertools import permutations

def solution(numbers):
    answer = 0

    #경우의 수 구하기
    list_str = list(numbers)
    case_set = set()
    for p in range(1, len(numbers)+1):
        case = list(map("".join, list(permutations(list_str, p))))
        for c in case:
            if int(c) > 1:
                case_set.add(int(c))

    # 소수인지 판독하기
    for number in case_set:
        flag = 0
        for num in range(2, number):
            if not number % num:
                flag = 1
                break
        if not flag:
            answer += 1
    return answer

