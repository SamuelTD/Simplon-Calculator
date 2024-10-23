from division import division
from multiplication import multiply
from addition import addition
from substraction import substraction

x = 0
y = 0

def get_input() -> int:
    """
    Ask user for two numbers. Keep asking until two valide numbers are inputed.    
    """
    #Keep asking the user for numbers until valid numbers are entered.
    while True:
        try:
            x = int(input("Veuillez entrer le premier nombre (entiers uniquement) :"))
            y = int(input("Veuillez entrer le deuxième nombre (entiers uniquement) :"))
            break
        except:
            print("Veuillez n'entrer que des chiffres entiers.")
    
    return x, y




def main():
    """
    Main function to run the program
    """
    #Keep going until the user close the program
    while True:
        
        #Keep asking the user for an operation until result is valid        
        while True:
            operation = input("What operation would you like to do? Please type operator : + - * /\nType quit to quit.")
            
            #Typing quit kill the program
            if operation.lower() == "quit":
                return
            
            #Check if input is one character long and is an accepted operator
            if len(operation) > 1 or operation not in "*/+-":
                print("Invalid operator. Please select +, -, * or / .")
            #If NOT loop    
            else:
                break
        
        #Get user's numbers
        x, y = get_input()

        #Call the right function depending on the user's operator
        if operation == "+":
            result = addition(x, y)
            print(f"The result of adding {x} to {y} is: {result}")

        if operation == "-":
            result = substraction(x, y)
            print(f"The result of substracting {x} from {y} is: {result}")


        if operation == "*":
            result = multiply(x, y)
            print(f"The result of multiplying {x} and {y} is: {result}")
    
        # if division here
        if operation == "/":
            result = division(x,y)
            print(f"The result of dividing {x} by {y} is: {result}")
        

if __name__ == "__main__":
    main()
