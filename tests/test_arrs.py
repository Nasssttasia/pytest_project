import pytest

from utils import arrs, dicts


@pytest.mark.parametrize('array, index, default, expected', [
    ([1, 2, 3], 1, "test", 2),
    ([], -1, "test", "test")
])

def test_get(array, index, default, expected):
    assert arrs.get(array, index, default) == expected


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3], -4) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -4, 1) == [1]
    assert arrs.my_slice([], 1, 1) == []


def test_get_val():
    assert dicts.get_val({'1': '2'}, '1', 'git') == '2'
    assert dicts.get_val({'1': '2'}, '3', 'git') == 'git'
    assert dicts.get_val({}, '1', 'git') == 'git'
