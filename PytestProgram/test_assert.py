import pytest


# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0
#
# def test_recursion_depth():
#     with pytest.raises(RuntimeError) as excinfo:
#
#         def f():
#             f()
#
#         f()
#     print(excinfo.value)
#     assert "maximum recursion" in str(excinfo.value)

# import pytest
#
#
# def myfunc():
#     raise ValueError("Exception 123 raised")
#
#
# def test_match():
#     with pytest.raises(ValueError, match=r".* 12 .*"):
#         myfunc()


# def test_set_comparison():
#     set1 = set("1308")
#     set2 = set("8031")
#     assert set1 == set2

class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2