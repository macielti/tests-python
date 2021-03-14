from .add import AddOperation
from faker import Faker

fake = Faker()

def test_sum():
    addOperation = AddOperation()
    number1 = fake.random_number()
    number2 = fake.random_number()

    output = addOperation.sum(number1, number2)

    expected_output = number1 + number2

    assert output == expected_output