def solution(my_string):
    answer = []
    d = ''
    for i in my_string:
        if i.isdigit():
            d += i
        else:
            if d:
                answer.append(int(d))
                d = ''
    if d :
        answer.append(int(d))
    if answer:
        return sum(answer)
    else:
        return 0
    
    ##다ㅣ시다시다시다싣사디