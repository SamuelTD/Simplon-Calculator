
def division(x: float, y: float) -> float | str:
    """
    Return the result of x divided by y  
    """ 
    #Vérifie qu'on ne divise pas par zéro. Si OUI retourne un message d'erreur
    if y == 0.0:
        return "ERROR : Impossible de divisier par zéro !"
    
    #Sinon retourne la division
    return x/y



