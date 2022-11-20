# Определение - Декоратор это функция, которая принимает аргументом функцию и возвращает функцию

# def decorator(func):
#     def wrapper():
#         print('here')
#         func()
#         print('there')
#     return wrapper


# !Функцию трогать Можно
def sum_lst(lst):
    return sum(lst)

# print(sum_lst([1, 2, 4, 5])) -> 12
# print(sum_lst([1, 2, 4, 5])) -> 6 сумма только четных чисел