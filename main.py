from division import division
from multiplication import multiply

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



x = 0
y = 0
def main():
    """
    Main function to run the program
    """
    operation = input("What operation would you like to do? ")
    get_input()


    # if addition here


    # if subtraction here



    if operation == "*":

        result = multiply(x, y)
        print(f"The result of multiplying {x} and {y} is: {result}")
    
    # if division here
    
    

    else:
        print("I don't know how to do that operation")

if __name__ == "__main__":
    main()
