from src.calculator import Calculator
from src.operations.add import AddOperation
from src.operations.sub import SubOperation

calc = Calculator(AddOperation(), SubOperation())
op1 = calc.add(2, 5, True)
op2 = calc.sub(5, 3, True)

print(op1)
print(op2)