from stack import Stack
import pytest

@pytest.fixture()
def data():
    return Stack()

def test_len():
    s = Stack()
    value = s.__len__()
    assert value == 0

def test_push(data):
    data.push(1)
    value = data.__len__()
    assert value == 1

def test_pop(data):

    data.push("Hello")
    data.push("World")
    value1 = data.pop()
    assert value1 == "World"
    value2 = data.pop()
    assert value2 == "Hello"


def test_pop2(data):
    data.push("Anjeli")
    data.push("Vijayan")
    value1 = data.pop()
    assert value1 == "Vijayan"
    value2 = data.pop()
    assert value2 == "Anjeli"




