import triangles
import pytest

many_triangles =  [(90,60,30,'right'),
                   (100,40,60,'obtuse'),
                   (60,60,60,'acute'),
                   (0,0,0,'invalid') ]
@pytest.fixture(params=many_triangles,ids = str)
def a_triangle(request):
        return request.param

def test_fixfunc(a_triangle):
    a,b,c,expected = a_triangle
    assert triangles.triangle_type(a,b,c)== expected

@pytest.mark.parametrize('a,b,c,expected',many_triangles)
def test_paramfunc(a,b,c,expected):
    assert triangles.triangle_type(a,b,c) == expected


