from division import division
from multiplication import multiply
from addition import addition
from substraction import substraction
from exponential import exponential

x = 0
y = 0

def get_input() -> int:
    """
    Ask user for two numbers. Keep asking until two valide numbers are inputed.    
    """
    #Keep asking the user for numbers until valid numbers are entered.
    while True:
        try:
            x = int(input("Enter the first number (integer only) :"))
            y = int(input("Enter the second number (integer only) :"))
            print("")
            break
        except:
            print("Please only input integer numbers.")
    
    return x, y




def main():
    """
    Main function to run the program
    """
    
    #Keep going until the user close the program
    while True:
        
        #Keep asking the user for an operation until result is valid        
        while True:
            operation = input("What operation would you like to do?\nPlease type operator : + - * / % **\nType quit to quit.\n")
            
            #Typing quit kill the program
            if operation.lower() == "quit":
                return
            
            #Check if input is exponential
            if operation == "**":
                break
            #Else check if input is one character long and is an accepted operator
            elif len(operation) > 1 or operation not in "*/+-%":
                print("Invalid operator. Please select +, -, *, /, ** or % .\n")   
            #If NOT loop    
            else:
                break
        
        #Get user's numbers
        x, y = get_input()

        #Call the right function depending on the user's operator
        if operation == "+":
            result = addition(x, y)
            print(f"The result of adding {x} to {y} is: {result}\n")

        if operation == "-":
            result = substraction(x, y)
            print(f"The result of substracting {x} from {y} is: {result}\n")


        if operation == "*":
            result = multiply(x, y)
            print(f"The result of multiplying {x} and {y} is: {result}\n")
    
        # if division here
        if operation == "/":
            result = division(x,y)
            print(f"The result of dividing {x} by {y} is: {result}\n")
         
        # if modulo here
        
        # if exponential here
        if operation == "**":
          result = exponential(x, y)
          print(f"The result of {x} exponent {y} is: {result}\n")
       

if __name__ == "__main__":
    main()
