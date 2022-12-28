from calc_2_task import calc

def test_calc_type():
    """
    Функция при правильном вводе параметров
    как итог должна вернуть: int, либо float (деление)
    При неправильном вводе - возвращается строка.

    """
    assert type(calc(2, 4, '+')) is int
    assert type(calc(8, 5, '-')) is int
    assert type(calc(4, 10, '*')) is int
    assert type(calc(10, 5, '/')) is float
    assert type(calc(2, 2, '**')) is int
    assert type(calc(10, 3, '%')) is int
    assert type(calc(20, 7, '//')) is int
    assert type(calc('nonsense', 'nonsense2', 'nonsense3')) is str
