import csv
import pytest
import triangles

def many_triangles():
    with open("triangle.csv") as csvfile:
        for a,b,c,expected in csv.reader(csvfile):
            print(f"Values are :",a,b,c,expected)
            yield (int(a),int(b),int(c),expected)

def test_print():
    (a,b,c,expected) = many_triangles()
    print(a,b,c,expected)


@pytest.mark.parametrize('a, b, c, expected ', many_triangles())
def test_func(a,b,c,expected):
    value = triangles.triangle_type(a,b,c)
    print(value)
    assert value == expected


