def solution(arr1, arr2):
    answer = []
    for x in range(len(arr1)):
        result = []
        for y in range(len(arr1[x])):
            result.append(arr1[x][y] + arr2[x][y])
        answer.append(result)
    return answer