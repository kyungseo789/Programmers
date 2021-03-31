from collections import deque
def solution(priorities, location):
    answer = 0
    result = []
    for i in range(len(priorities)):
        result.append((priorities[i], i))

    pri_deq = deque(result)
    print_order = 1
    while pri_deq:
        tmp = pri_deq.popleft()
        if pri_deq and tmp[0] < max(pri_deq)[0]:
            pri_deq.append(tmp)
            continue
        if tmp[1] == location:
            answer = print_order
            break
        print_order += 1
    return answer