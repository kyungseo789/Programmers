def solution(answers):
    answer = []

    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_cnt = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            answer_cnt[0] += 1

        if answers[i] == b[i % len(b)]:
            answer_cnt[1] += 1

        if answers[i] == c[i % len(c)]:
            answer_cnt[2] += 1

    for j in range(len(answer_cnt)):
        if answer_cnt[j] == max(answer_cnt):
            answer.append(j+1)

    return answer