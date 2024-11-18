def solution(n):
    answer = 0
    prev, curr = 0, 1
    for i in range(n-1):
        answer = prev + curr
        prev = curr
        curr = answer
    return answer % 1234567