import homework_scripts_1_task as hm_sc1

def test_string():
    assert hm_sc1.strr('ДОМ') == 'МО'

def test_string_2():
    assert hm_sc1.strr('example string') == 'gn'

def test_string_3():
    assert hm_sc1.strr('What you think you become') ==  'em'

def test_func_sum_of_lists():
    assert hm_sc1.func([1, 2, 3],[4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_func_sum_of_int_and_float():
    assert hm_sc1.func(2.2, 4, 8, 19.5) == 33.7

def test_func_sum_of_strings():
    assert hm_sc1.func('abc', '123', 'hjk', '$$$') == 'abc123hjk$$$' 

def test_fibonacci_5():
    assert hm_sc1.fibonacci(5) == 5

def test_fibonacci_2_15():
    assert hm_sc1.fibonacci(15) == 610

def test_fibonacci_3_22():
    assert hm_sc1.fibonacci(22) == 17711
