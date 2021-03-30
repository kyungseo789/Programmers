def solution(name):
    answer = 1e+10
    alpha = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
        "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
        "M": 12, "N": 13, "O": 12, "P": 11, "Q": 10, "R": 9,
        "S": 8, "T": 7, "U": 6, "V": 5, "W": 4, "X": 3, "Y": 2, "Z": 1
    }
    order_idx = list(_ for _ in range(len(name)))
    order_back = list(_ for _ in range(len(name)-1,-1,-1))
    for i in range(len(order_idx)):
        order_list = order_idx[i:] + order_idx[:i]
        tmp_cnt = 0
        move_cnt = len(name) - 1
        for j in range(len(order_list)):
            if j == 0 and name[order_list[j]] == 'A':
                move_cnt -= 1
            elif 0 < j < len(name)-1 and name[order_list[j-1]] == 'A' and name[order_list[j]] == 'A':
                move_cnt -= 1
            tmp_cnt += alpha.get(name[order_list[j]])
        if answer > tmp_cnt + move_cnt:
            answer = tmp_cnt + move_cnt
    for i in range(len(order_back)):
        order_list = order_back[i:] + order_back[:i]
        tmp_cnt = 0
        move_cnt = len(name) - 1
        for j in range(len(order_list)):
            if j == 0 and name[order_list[j]] == 'A':
                move_cnt -= 1
            elif 0 < j < len(name)-1 and name[order_list[j-1]] == 'A' and name[order_list[j]] == 'A':
                move_cnt -= 1
            tmp_cnt += alpha.get(name[order_list[j]])
        if answer > tmp_cnt + move_cnt:
            answer = tmp_cnt + move_cnt
    return answer