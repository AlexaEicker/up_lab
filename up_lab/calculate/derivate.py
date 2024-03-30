from sympy import symbols, diff, simplify

#TODO: check wheter this is multiple derivatives and wheter I need higher derivatives somewhere

def derivatives():
    '''
    Calculates derivatives of typed in formula.
    The formula and variables are asked during the process.
    
    Return:
    list: List of all derivatives 
    
    '''

    formula = input("Enter the formula (python - style): ")
    variables = input("Enter the variables in the formula (comma-separated): ").split(',')

    syms = symbols(variables)
    derivatives = [simplify(diff(formula, sym)) for sym in syms]

    for var, derivative in zip(variables, derivatives):
        print(f"Derivative of {formula} with respect to {var}: {derivative}")
    return derivatives
