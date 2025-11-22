def solution(my_string):
    my_string = my_string.split()
    result=int(my_string[0])
    for i, d in enumerate(my_string):
        
        if d == "+":
            result += int(my_string[i+1])
        elif d == "-":
            result -= int(my_string[i+1])
    return result