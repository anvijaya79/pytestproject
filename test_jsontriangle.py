import json
import pytest
import triangles

def a_triangle():
    with open("triangle.json") as  file:
        for a,b,c,expected in json.load(file):
            yield(int(a),int(b),int(c),expected)

@pytest.mark.parametrize('a,b,c,expected',a_triangle())
def test_triangle(a,b,c,expected):
    value = triangles.triangle_type(a,b,c)
    assert value == expected
