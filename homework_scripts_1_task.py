#!/usr/bin/python3

def strr(string):
    return string[-1:-3:-1]


import functools


def func(*args):
    """Сумма произвольного количества параметров
        Принимает:
            *args - число, строка, список в произвольном количестве.
        Возвращает:
            Сумму параметров
    """
    # В функции можно суммировать int, float, string, list, tuple
    # с помощью модуля functools и его функции reduce
    # которая принимает функцию, которую требуется применить
    # к элементам последовательности
    # и последовательность, элементы которой
    # требуется свести к единственному значению
    return functools.reduce((lambda x, y: x + y), args)


def fibonacci(n):
    """Нахождение числа Фибоначчи
    Принимает:
        n - число (номер позиции искомого числа Фибоначчи)
    Возвращает:
        Искомое число Фибоначчи
    """
    # Первые два числа Фибоначчи 0 и 1:
    if (n <= 1):
        return n
    else:
        # Каждое следующее число равно сумме двух предыдущих:
        return (fibonacci(n-1) + fibonacci(n-2))
