def solution(nums):
    answer = 0
    nums_kind = set(nums)
    answer = min(len(nums_kind), len(nums)/2)
    return answer