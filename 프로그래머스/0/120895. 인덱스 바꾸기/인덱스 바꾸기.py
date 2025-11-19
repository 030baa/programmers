def solution(my_string, num1, num2):
    answer = ''
    str1 = my_string[num1]
    str2 = my_string[num2]
    for i in range(len(my_string)):
        if i == num1:
            answer += str2
        elif i == num2:
            answer += str1
        else:
            answer += my_string[i]
    return answer


#문자열의 경우. 할당되지 않음
#리스트는 할당이 됨!
#따라서 자료형을 리스트로 변환해서 사용하자.
#my_string = list(my_string)
#my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
#''.join(my_string)
