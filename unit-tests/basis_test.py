from basis import *

def test_CardinalSplineOrderOne():
    basis = CardinalSpline(1,1,0)

    assert 0.0 == basis(31.0)
    assert 0.0 == basis(0.0)
    assert 0.0 == basis(2.0)
    assert 1.0 == basis(1.0)
    assert 0.5 == basis(1.5)
    assert 0.5 == basis(0.5)

def test_CardinalSplineOrderTwo():
    basis = CardinalSpline(2,1,0)
    assert 0.0 == basis(0.0)
    assert 0.0 == basis(3.0)
    assert 0.5 == basis(1.0)
    assert 0.5 == basis(2.0)
    assert 0.75 == basis(1.5)
