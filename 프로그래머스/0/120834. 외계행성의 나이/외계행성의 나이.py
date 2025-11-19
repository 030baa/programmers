def solution(age):
    en = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([en[int(i)] for i in str(age)])