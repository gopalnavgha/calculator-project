import pytest
from calculator import calculators
from django.urls import reverse

def test_add():
    assert calculators.add(2,3) == 5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculators.div(1,0)

def test_sqrt_negative():
    with pytest.raises(ValueError):
        calculators.sqrt(-4)

def test_area_circle():
    r = 2
    assert pytest.approx(calculators.area_circle(r), rel=1e-6) == 3.141592653589793 * 4

def test_quadratic_roots_real():
    r1, r2 = calculators.quadratic_roots(1, -3, 2)
    assert set([round(r1,6), round(r2,6)]) == set([1.0, 2.0])

@pytest.mark.django_db
def test_index_view_calculation(client):
    url = reverse('calculator_index')
    resp = client.post(url, data={'operation':'add','x':2,'y':5})
    assert resp.status_code == 200
    assert b'Result' in resp.content
    assert b'7' in resp.content
