
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
        else:
            return False
        
    def number_entry(self):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        return num1, num2
    
    def retry(self):
        yes_no = input("\nDo you wish to continue? (yes or no): ")
        print("\n------------------------------------------------------------------------------------------------------------------")
        if yes_no == "no":
            print("\n\t\t\t\t       THANKS YOU!")
            print("\n------------------------------------------------------------------------------------------------------------------")

    def Addition(self,num1,num2):
    #ADD
        return num1+num2

    def Subtraction(self,num1,num2):
    #subtract
        return num1-num2
    def multiply(self,num1,num2):
    #multiply
        return num1*num2

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