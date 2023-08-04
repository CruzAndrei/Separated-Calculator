#mainpage
from Calculator import Calcu

simple_calculator = Calcu()
simple_calculator.Operations()

operation = {
    "+": simple_calculator.Addition,    
    "-": simple_calculator.Subtraction,
    "*": simple_calculator.Multiplication,
    "/": simple_calculator.Division
}