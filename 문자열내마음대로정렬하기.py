def solution(strings, n):
    answer = []
    idx_strings = []
    for string in strings:
        idx_strings.append((string[n], string))
    idx_strings = sorted(idx_strings, key=lambda x: (x[0], x[1]))
    
    for i in idx_strings:
        answer.append(i[1])
    return answer