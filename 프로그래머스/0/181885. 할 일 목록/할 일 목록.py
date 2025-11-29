def solution(todo_list, finished):
    answer = []
    return [todo for todo, finish in zip(todo_list,finished) if finish == False]