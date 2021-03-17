def solution(array, commands):
    answer = []
    N = len(commands)
    for n in range(N):
        i,j,k = commands[n]
        result = array[i-1:j]
        result.sort()
        answer.append(result[k-1])
    return answer