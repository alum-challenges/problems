from telescope import zoom
import pytest

def test_zoom():
    assert zoom(3, 5) == 15.0
    assert zoom(5, 3) == 15.0
    assert zoom(1.77, 3.5) == 6.195
    assert zoom(1, 1) == 1.0
    assert zoom(1.225, 1) == 1.225
