from .calculator import Calculator
from .operations.test.add import AddOperationSpy
from .operations.test.sub import SubOperationSpy
from faker import Faker

fake = Faker()


def test_add():
    addOperation = AddOperationSpy()
    calculator = Calculator(addOperation, SubOperationSpy())
    number1 = fake.random_number()
    number2 = fake.random_number()

    result = calculator.add(number1, number2, True)

    # Input test
    assert addOperation.sum_attributer["number1"] == number1
    assert addOperation.sum_attributer["number2"] == number2

    # Test output
    assert result is not None

def test_add_none():
    addOperation = AddOperationSpy()
    calculator = Calculator(addOperation, SubOperationSpy())
    number1 = fake.random_number()
    number2 = fake.random_number()

    result = calculator.add(number1, number2, False)

    # Input test
    assert addOperation.sum_attributer == {}

    # Test output
    assert result is None

def test_sub():
    subOPeration = SubOperationSpy()
    calculator = Calculator(AddOperationSpy(), subOPeration)
    number1 = fake.random_number()
    number2 = fake.random_number()

    result = calculator.sub(number1, number2, True)

    # Test input
    assert subOPeration.difference_attributer["number1"] == number1
    assert subOPeration.difference_attributer["number2"] == number2

    # Test output
    assert result is not None

def test_sub_none():
    subOPeration = SubOperationSpy()
    calculator = Calculator(AddOperationSpy(), subOPeration)
    number1 = fake.random_number()
    number2 = fake.random_number()

    result = calculator.sub(number1, number2, False)

    # Test input
    assert subOPeration.difference_attributer == {}

    # Test output
    assert result is None