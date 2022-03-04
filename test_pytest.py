# import pytest
# def sum(num1,num2):
#  return num1 + num2
#
# def test_sum_int():
#  assert sum(1,2) == 3
#
# def test_sum_str():
#  assert sum('1','2') == '12'
#
# def test_bad():
#  assert  sum(1,2) ==2
#
# @pytest.mark.parametrize(
#  'num1,num2,eq_num',
#  [
#   (1,2,3),
#   (4,5,9),
#   (0,0,0)
#  ]
# )
# def test_multi_sum(num1,num2,eq_num):
#  assert sum(num1,num2) == eq_num

import pytest


def test_sample1():
    assert 1 == 1


def test_sample2():
    assert [1, 2, 3] == [3, 2, 1]


@pytest.mark.xfail()
def test_sample3():
    assert 1 != 1


@pytest.mark.xfail()
def test_sample4():
    assert 1 == 1