from faker import Faker

fake = Faker()

class SubOperationSpy:

    def __init__(self):
        self.difference_attributer = {}

    def difference(self, number1, number2):
        self.difference_attributer["number1"] = number1
        self.difference_attributer["number2"] = number2
        
        return fake.random_number()