from division import division
from multiplication import multiply
from addition import addition
from substraction import substraction
from exponential import exponential

x = 0
y = 0

def get_input() -> None:
    """
    Ask user for two numbers. Keep asking until two valide numbers are inputed.    
    """
    #Keep asking the user for numbers until valid numbers are entered.
    while True:
        try:
            x = float(input("Veuillez entrer le premier nombre :"))
            y = float(input("Veuillez entrer le deuxième nombre :"))
            break
        except:
            print("Veuillez n'entrer que des chiffres.")




def main():
    """
    Main function to run the program
    """
    operation = input("What operation would you like to do? ")
    get_input()


    # if addition here
    if operation == "+":

        result = addition(x, y)
        print(f"The result of adding {x} to {y} is: {result}")

    # if subtraction here
    if operation == "-":

        result = substraction(x, y)
        print(f"The result of substracting {x} from {y} is: {result}")

    # if multiplication here
    if operation == "*":

        result = multiply(x, y)
        print(f"The result of multiplying {x} and {y} is: {result}")
    
    # if division here
    
    
    # if modulo here
    # if exponential here
    if operation == "**":

        result = exponential(x, y)
        print(f"The result of {x} exponent {y} is: {result}")
    else:
        print("I don't know how to do that operation")

if __name__ == "__main__":
    main()
