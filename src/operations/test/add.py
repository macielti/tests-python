from faker import Faker

fake = Faker()

class AddOperationSpy:

    def __init__(self):
        self.sum_attributer = {}

    def sum(self, number1, number2):
        self.sum_attributer["number1"] = number1
        self.sum_attributer["number2"] = number2
        
        return fake.random_number()
    