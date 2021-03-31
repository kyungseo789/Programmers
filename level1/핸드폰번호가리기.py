def solution(phone_number):
    length = len(phone_number)
    answer = '*'*(length-4)
    answer += phone_number[length-4:length]
    return answer