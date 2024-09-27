def solution(nums):
    up = set(nums)
    answer = min(len(up), len(nums)//2)
    return answer