def solution(n_str):
    for i in n_str:
        if i != "0":
            idx = n_str.index(i)
            return n_str[idx:]
    