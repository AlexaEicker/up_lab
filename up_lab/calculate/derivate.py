from sympy import symbols, diff, simplify
import fitting.basic_functions as basic_functions


def derivatives(formula=None, variables=None):
    '''
    Calculates derivatives of typed in formula.
    The formula and variables are asked during the process.
    ===========================

    Arg:
    formula (optional): callable
    variables (optional): list of str.
        Every entry is name of a variable that 
        
    Return:
    list: List of all derivatives 
    
    '''

    if formula ==None:
        formula = input("Enter the formula (python - style): ")
        variables = input("Enter the variables in the formula (comma-separated): ").split(',')
    else:
        formula = basic_functions.function_availibility
        if formula==None:
            raise ValueError("No function choosen.")
        else:
            pass

    syms = symbols(variables)
    derivatives = [simplify(diff(formula, sym)) for sym in syms]

    for var, derivative in zip(variables, derivatives):
        print(f"Derivative of {formula} with respect to {var}: {derivative}")
    return derivatives
