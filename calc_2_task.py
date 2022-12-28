#!/usr/bin/python3

def calc(a, b, operation):
    """Калькулятор чисел
    Принимает:
        a - первое число
        b - второе число
        operation - действие над числами
    Возвращает:
        Результат операции над числами
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    elif operation == '**':
        return a ** b
    elif operation == '%':
        return a % b
    elif operation == '//':
        return a // b
    else:
        return (f'wrong operator')
