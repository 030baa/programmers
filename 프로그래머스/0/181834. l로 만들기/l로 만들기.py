def solution(myString):
    eng = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in myString:
        if eng.index(i) < eng.index("l"):
            answer += "l"
        else:
            answer += i
    return answer