def solution(s):
    p_cnt = 0
    y_cnt = 0
    
    s = s.lower()
    for i in s:
        if i == "p":
            p_cnt += 1
        elif i == "y":
            y_cnt += 1
    
    return True if p_cnt == y_cnt else False