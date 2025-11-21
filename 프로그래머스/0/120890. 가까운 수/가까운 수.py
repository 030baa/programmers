def solution(array, n):
    dif = []
    for i in array:
        dif.append((i, abs(n-i)))
    dif = sorted(dif, key=lambda x : (x[1], x[0]))
    return dif[0][0]
    