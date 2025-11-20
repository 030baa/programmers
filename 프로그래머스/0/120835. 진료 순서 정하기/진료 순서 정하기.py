def solution(emergency):
    answer = []
    em_sorted = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(em_sorted.index(i) + 1)
    return answer