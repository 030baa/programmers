def solution(my_string, letter):
    #my_string.replace(letter,'')
    return ''.join([i for i in my_string if i != letter])