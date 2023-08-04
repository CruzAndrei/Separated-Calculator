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

while True:
    option = simple_calculator.operation_to_use()

    if simple_calculator.operation_within(option):
        try:
            first_number, second_number = simple_calculator.number_entry()
        except ValueError:
            print("Invalid Input")
            continue

        result = operation[option](first_number,second_number)
        print("\nThe result is : " + str(result))

        if simple_calculator.retry():
            break
    else:
        print("invalid input")
