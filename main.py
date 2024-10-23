import multiplication

def main():
    """
    Main function to run the program
    """
    operation = input("What operation would you like to perform? ").lower()


    # if addition here


    # if subtraction here



    if operation in ["multiplication", "*", "x", "multiply"]:
        try:
            number_1 = int(input("Enter the first number to multiply: "))
            number_2 = int(input("Enter the second number to multiply: "))
        except ValueError:
            print("Please enter valid integers.")
            return

        result = multiplication.multiply(number_1, number_2)
        print(f"The result of multiplying {number_1} and {number_2} is: {result}")
    
    # if division here
    
    
    
    
    
    else:
        print("I don't know how to do that operation")

if __name__ == "__main__":
    main()