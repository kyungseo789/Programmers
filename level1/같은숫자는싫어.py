def solution(arr):
    answer = []

    if len(arr) == 1:
        return arr
    
    if len(arr) == 2:
        if arr[0] == arr[-1]:
            return [arr[0]]
        return arr
    
    tmp = arr[0]
    for i in range(1, len(arr)):
        if tmp != arr[i]:
            answer.append(tmp)
            tmp = arr[i]
    answer.append(tmp)
    return answer