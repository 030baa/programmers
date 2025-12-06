def solution(a, d, included):
    count = a
    answer = [a]
    for i in range(len(included)-1):
        count += d
        answer.append(count)
    return sum([answer[idx] for idx, inc in enumerate(included) if inc == True ])