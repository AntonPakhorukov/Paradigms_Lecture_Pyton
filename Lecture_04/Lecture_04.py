# объявить новый список, взять элемент, получить остаток деления,
# положить в новый список и продолжать так до конца полученного списка.
# ver.1
# DIVISION_NUM = 5
# arr = [i for i in range(20)]
# res = []
# for el in arr:
#     res.append(el % DIVISION_NUM)
# print(arr)
# print(res) 
# # ver.2
# DIVISION_NUM = 5
# arr = [i for i in range(20)]
# modulo = lambda x: x % DIVISION_NUM
# res = list(map(modulo, arr))
# print(res)

# Функцию можно сделать “нечистой”, если нарушится одно из условий.
# Например, если функция будет зависеть от чего-то чего нет 
# в её сигнатуре:
# x = 5
# def pow(y):
#     return x * y
# print(pow(5))

# Функциональное программирование позволяет писать так называемые 
# функции высшего порядка - то есть такие, которые могут принимать 
# и возвращать другие функции.
# def function_getter(func):
#     print("I got the function: ", func.__name__)
#     return func
# function_getter(map)

# в Python есть функционал, позволяющий работать с ленивыми 
# вычислениями: создавать собственные ленивые функции и вызывать 
# их пошагово. Этот функционал реализован с помощью генераторов
# - функций, которые возвращают по одному объекту за один вызов.
# def lazy_function():
#     i = 0
#     while True:
#         yield i
#         i += 1
# f = lazy_function()
# print(next(f)) # 0
# print(next(f)) # 1
# print(next(f)) # 2
# print(next(f)) # 3

# Вот у нас есть функция двух аргументов, возвращающая сумму 
# за один вызов add.
# def add(x, y):
#     return x + y
# print(add(2, 5))
# Применим каррирование к этой функции.
# def add2(x):
#     def add2_x(y):
#         return x + y
#     return add2_x
# print(add2(3)(5))

# мы видим процедуру sum_squares, которая принимает переменную
# lst типа список и возвращает число int
# def sum_squares(lst: list) -> int:
#     return sum(map(lambda x: x ** 2, lst))
# list = {1, 2, 3, 4, 5}
# print(sum_squares(list))
# <<< Haskell реализция >>>
# sumSquares = sum . map (^2)
# <<< Структурно-процедурная реализация >>>
# def sum_squares(lst: list) -> int:
#     current_sum = 0
#     for el in lst:
#         current_sum += (el ** 2)
#     return current_sum
# list = {1, 2, 3, 4, 5}
# print(sum_squares(list))
# <<<ООП реализация>>>
# class List:
#     def __init__(self, lst):
    #     self.lst = lst
    # def calculate_sum_squares(self):
    #     current_sum = 0
    #     for el in self.lst:
    #         current_sum += (el ** 2)
    #     self.calculate_sum_squares = current_sum
# <<<ООП реализация + ыункциональный подход>>>
# class List:
#     def __init__(self, lst):
#         self.lst = lst
#     def calculate_sum_squares(self):
#         self.sum_squares = sum(map(lambda x: x ** 2, self.lst))
# print(List.calculate_sum_squares()) 

# <<<Функция композиция>>>
def compose(f, g):
    return lambda x: f(g(x))
print(compose(4, 5))  
# Haskell
# compose f g x = f (g x)
# f :: Int -> Int
# f x = x * 2     
# g :: Int -> Int
# g x = x + 3
# h :: Int -> Int
# h = compose f g