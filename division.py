
def division(x: float, y: float) -> float | str:
    """
    Return the result of x divided by y  
    """ 
    RED = "\033[91m"
    
    #Vérifie qu'on ne divise pas par zéro. Si OUI retourne un message d'erreur
    if y == 0.0:
        return (f"{RED}ERROR : Cannot divide by zero!")
    
    #Sinon retourne la division
    return x/y



