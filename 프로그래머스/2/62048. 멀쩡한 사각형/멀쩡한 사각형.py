def solution(w,h):
    r = euclidean(w, h)
    nw, nh = w // r, h // r
    block = nw + nh - 1
    answer = w*h - (block * r)
    return answer

def euclidean(a, b):
    if b == 0:
        return a
    return euclidean(b, a%b)