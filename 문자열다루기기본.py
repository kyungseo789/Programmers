def solution(s):
    answer = True
    string_length = len(s)
    if s.isnumeric() and (string_length == 4 or string_length == 6):
        return answer
    answer = False
    return answer