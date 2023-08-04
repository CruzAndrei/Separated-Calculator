
class Calcu():
    def Operations(self):
        print("Here are the basic math operation to be used:")
        print("+ ADD")
        print("- SUBTRACT")
        print("* MULTIPLY")
        print("/ DIVIDE")

    def operation_to_use(self):
        basic_operation = input("Select operation to be executed: ")
        return basic_operation

    def operation_within(self,basic_operation):
        if basic_operation in ('+', "-", "*", "/"):
            return True



    #ADD
        if basic_operation == "+":
            data_operation = first_num + second_num
            print("The sum of your inputed number is ", data_operation)
    #subtract
        elif basic_operation == "-":
            data_operation = first_num - second_num
            print("The difference of your inputed number is ", data_operation)
    #multiply
        elif basic_operation == "*":
            data_operation = first_num * second_num
            print("The product of your inputed number is ", data_operation)
    #divide
        elif basic_operation == "/":
                try:
                    data_operation = first_num / second_num
                    print("The quotient of your inputed number is ", data_operation)
                except ZeroDivisionError as ERROR:
                    print("Second number must not be zero")
                    print("Invalid Equation")
                    print("ERROR")
                    print("Try again")
                    return
        else:
            print("Invalid Operation")