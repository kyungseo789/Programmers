def solution(a, b):
    answer = ''
    monthly_days = [31,29,31,30,31,30,31,31,30,31,30,31]
    day_of_week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    daily = b
    #월 단위로 일수 더하기
    for i in range(a-1):
        daily += monthly_days[i]
    daily %= 7
    answer = day_of_week[daily]
    return answer