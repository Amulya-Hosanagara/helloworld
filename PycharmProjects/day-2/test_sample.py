def func(x):
    return x +1

def add(x, y):
    return x+y

def test_answer():
    assert func(3)== 5

def test_method():
    assert add(3,5) == 8
    assert add(3,4) ==7
