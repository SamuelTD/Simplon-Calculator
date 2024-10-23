import multiplication

x = 0
y = 0
def main():
    """
    Main function to run the program
    """
    operation = input("What operation would you like to perform? ").lower()


    # if addition here


    # if subtraction here



    if operation == "*":

        result = multiplication.multiply(x, y)
        print(f"The result of multiplying {x} and {y} is: {result}")
    
    # if division here
    
    
    
    
    
    else:
        print("I don't know how to do that operation")

if __name__ == "__main__":
    main()