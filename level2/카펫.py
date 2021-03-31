def solution(brown, yellow):
    answer = []
    x = 3
    x_max = int((brown + 4) / 2 - 1)
    y = int((brown - 2*x + 4) / 2)

    for i in range(3, x_max +1):
        if (x-2) * (y-2) == yellow:
            answer.append(y)
            answer.append(x)
            break
        x += 1
        y = int((brown - 2 * x + 4) / 2)
    return answer