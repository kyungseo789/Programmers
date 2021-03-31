from collections import deque
def solution(priorities, location):
    answer = 0
    pri_deq = deque([(value,idx) for idx,value in enumerate(priorities)])
    while pri_deq:
        tmp = pri_deq.popleft()
        if pri_deq and tmp[0] < max(pri_deq)[0]:
            pri_deq.append(tmp)
        else:
            answer += 1
            if tmp[1] == location:
                break
    return answer