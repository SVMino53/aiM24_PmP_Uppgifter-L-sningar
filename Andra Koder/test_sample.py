import pytest


def add(x, y):
    return x + y

def sub(x, y):
    return x - y


def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 1) == 4

def test_add_mirror():
    assert add(2, 3) == add(3, 2)

def test_sub_mirror():
    assert sub(2, 3) != sub(3, 2)

def test_add_type_error():
    with pytest.raises(TypeError):
        add('2', 3)