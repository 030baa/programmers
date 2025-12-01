def solution(ineq, eq, n, m):
    answer = ""
    if eq == "!":
        answer = str(n) + ineq + str(m)
        return int(eval(answer))
    else:
        answer = str(n) + ineq + eq + str(m)
        return int(eval(answer))