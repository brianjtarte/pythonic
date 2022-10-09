import pytest
from pythonic.pythonic import Stack


# @pytest.mark.skip("TODO")
def test_exists():
    assert Stack


# @pytest.mark.skip("TODO")
def test_push_string():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_reverse_string():
    s = Stack()
    new_string = "elppa"
    actual = s.reverse_string(new_string)
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_pop_string():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected
