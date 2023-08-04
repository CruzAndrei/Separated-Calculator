
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
        first_number = float(input("Enter your first number: "))
        second_number = float(input("Enter your second number: "))
        return first_number, second_number
    
    def retry(self):
        yes_no = input("\nDo you wish to continue? (yes or no): ")
        print("\n------------------------------------------------------------------------------------------------------------------")
        if yes_no == "no":
            print("\n\t\t\t\t       THANKS YOU!")
            print("\n------------------------------------------------------------------------------------------------------------------")

    def Addition(self,first_number,second_number):
    #ADD
        return first_number + second_number

    def Subtraction(self,first_number,second_number):
    #subtract
        return first_number - second_number
    def Multiplication(self,first_number,second_number):
    #multiply
        return first_number * second_number
    def Division(self,first_number,second_number):
    #divide
            try:
                first_number / second_number
            except ZeroDivisionError as ERROR:
                print("Second number must not be zero")
                print("Invalid Equation")
                print("ERROR")
                print("Try again")
                return        
            return first_number / second_number