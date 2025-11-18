def solution(my_string, letter):
    answer = ''
    return ''.join([i for i in my_string if i != letter])