from division import division

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



