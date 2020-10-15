from yaml import load, dump
import pytest
import triangles

def a_triangle():
  with open('triangle.yaml') as test:
    for a,b,c,expected in load(test):
            print(f"Values are :", a, b, c, expected)
            yield (int(a), int(b), int(c), expected)

@pytest.mark.parametrize('a,b,c,expected',a_triangle())
def test_func(a,b,c,expected):
      value = triangles.triangle_type(a,b,c)
      assert value == expected

