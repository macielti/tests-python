from .sub import SubOperation
import pytest

subOperation = SubOperation()


@pytest.mark.parametrize('num1, num2, result',
                         [
                             (3, 2, 1),
                             (4, 1, 3)
                         ]
                         )
def test_difference(num1, num2, result):

    assert subOperation.difference(num1, num2) == result
