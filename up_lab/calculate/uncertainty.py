import numpy as np
from scipy.stats import t
from basic_calc import type_change
from sympy import symbols, diff, simplify
import fitting.basic_functions as basic_functions


def derivatives(formula=None, variables=None, printderivatives = True):
    '''
    Calculates derivatives of typed in formula.
    The formula and variables are asked during the process.
    ===========================

    Arg:
    formula (optional): callable.
        formula that determines size, of which the uncertainty should be calculated.
    variables (optional): list of str.
        Every entry is name of a variable that is measured.
    printderivatives (optional): boolean.
        Default: True
        Disables print of all derivatives.
        
    Return:
    derivatives: List of all derivatives. 
    syms: list of all variables converted to sympy symbols.
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

    if printderivatives:
        print(f"Derivatives of {formula} :")
        for var, derivative in zip(variables, derivatives):
            print(f"With respect to {var}: {derivative}")
    return derivatives,syms


def type_a(values):
    ''' Calculates type A uncertainty

    Type A uncertainty according to ISO/IEC Guide 98-3
    ==========================

    Args:
    values: measured values taken in the experiment; numpy-array
    ==============

    Return:
    float
    '''

    values = type_change(values,np.array)
    N=len(values)
    values_mean=np.mean(values)
    values_sum=sum((values-values_mean)**2)
    unc_typea= (1/(N-1)*values_sum)**(1/2)/(N**(1/2))

    # Calculate student factor for a confidence level of 68.3%  (typical for physics)
    if N<=100:
        student_factor = t.ppf(0.8415, df=N+1)
        unc_typea=student_factor*unc_typea
    return unc_typea
    
def type_b(b=float, method=str):
    '''
    Calculates type B uncertainty according to ISO/IEC Guide 98-3
    ========================
    
    Args:
    b: Display increment as float
    method: 'digital' or 'analog' depending of the type of measuring.
    =====================

    Return:
    float
    '''

    if method=='digital':
        unc_typeb = b/(2*3**(1/2))
    elif method=='analog':
        unc_typeb= b/(2*6**(1/2))
    else:
        print("Your method could not be determined. Please type 'digital' or 'analog'")
    return unc_typeb

def device_acuracy(values,method=str, percentage=float, digit=int, scale_end=float):
    '''Calculates the uncertainty of a device by the acuracy given by the producer.
    ============================
    
    Args:
    values: Array - like.
        Array of values taken during the experiment
    method: str.
      'analog' or 'digital' device
    percentage: float
        indicated acuracy. CAUTION: give as decimal 
            Ex: 2.0% please enter 0.02
    digit: int.
        increasment by digits (given by producer). 
    scale_end: float.
        Only needed with analog device. End of scale. 
    ======================

    Return:
    float or numpy array
    '''

    values = type_change(values, np.array)
    if method=='analog':
        unc_device = percentage * scale_end
    elif method=='digital':
        unc_device = np.zeros(len(values))
        for i in range(len(values)):
            valnumber = values[i]
            if type(valnumber)==int:
                digitinc = digit
            else:
                valnumber_list = str(valnumber).split('.')
                digitinc = digit * 10**(-len(valnumber_list[1]))
                
            unc_device[i] = values[i]*percentage + digitinc
    return unc_device


def combined_unc(uncertainties):
    '''Calculates the combined uncertainty of taken values. 
    The combined standard uncertainty is the square root of the sum of the squares of individual standard uncertainties (Type A and Type B uncertainties).
    Added to that, in the same manner, are all other known uncertainties which resultes in a final uncertainty of the measurment.
    ======================

    Args:
    uncertainties: list, numpy - Array or dictionary
        list of all known uncertainties
    ===================================
    
    Return:
    Combined uncertainty as float

    For a detailed explanation of Type A and Type B uncertainty see the functions 'type_a' and 'type_b'
    '''

    uncertainties = type_change(uncertainties, list)
    unc = sum(x**2 for x in uncertainties)**(1/2)
    return unc


def expanded_unc(uncertainty, factor=int):
    '''Calculates expanded uncertainty.
    =================================
    
    Args:
    uncertainty: list or float
    factor: integer
        Scales the expansion of the uncertainty
    ===================
    
    Return:
    list or float, depending on type of given uncertainty'''

    return uncertainty*factor



def error_propagation(alldata, uncertainties,type='linear', formula=None, variables=None):
    '''
    Calculates the uncertainty according to linear and gaussian law of propagation of measurement uncertainties.
    This is needed when the variable is defined by the taken measurement variables. 
    Ex: s = v*t. v and t are measured. This calculation is necessary, if you are looking for s.
    ===========================

    Args:
    alldata: List of Array - likes
        All datasets the variable depends on in the EXACT same order as the uncertainties and variables.
        If no variables are defined yet they will be requested during the function.
    uncertainties: Array - like or float
        Uncertainties of all variables needed to calculate the uncertainty of variable. 
        If a variable is given or doesn't have an uncertainty, add '0' to your list.
    type: str
        'linear' or 'gaussian' for the respective type of error propagation. See explanation below.
        Default: linear
    formula: callable (optional)
        formula that determines size, of which the uncertainty should be calculated.
    ==========

    Return:
    numpy array of error propagation for every variable set.
    ===============

    Linear error propagation:
    Use when the relationship between the variables and the function of interest is approximately linear,
    and the uncertainties are small relative to the values of the variables.

    Gaussian error propagation:
    Use when the variables are not necessarily linearly related, but the uncertainties are assumed to follow a Gaussian distribution.
    This method is applicable when dealing with a large number of independent and identically distributed random variables.
    '''
    
    k=0
    error_prop = np.array
    uncertainties = type_change(uncertainties, list)
    derivate, varsymbol = derivatives(formula, variables, printderivatives=False)
    if len(derivate)<len(uncertainties):
        raise ValueError("You entered LESS variables to derivate to than you have uncertainties. This does not work. Please check your formula, your variables and the uncertainties you entered.")
    elif len(derivate)>len(uncertainties):
        raise ValueError("You entered MORE variables to derivate to than you have uncertainties. This does not work. Please check your formula, your variables and the uncertainties you entered.")
    else:
        if type=='linear':
            for k in range(0, len(alldata[0])):
                derval = 0
                for i in range(0,len(derivate)):
                    workingvar = varsymbol[i]
                    workingval = alldata[i][k]
                    derval+=derivate[i].subs(workingvar, workingval)*uncertainties[i]
                error_prop[k]=derval
        elif type=='gaussian':
            for k in range(0, len(alldata[0])):
                derval =0
                for i in range(0,len(derivate)):
                    workingvar = varsymbol[i]
                    workingval = alldata[i][k]
                    derval += (derivate[i].subs(workingvar,workingval)*uncertainties[i])**2
                error_prop[k]=derval
        else:
            raise ValueError("Wrong type. Please type 'linear' or 'gaussian'.")
    return error_propagation


def uncertainty(data, b=0, method=str, percentage=float, digit=int, scale_end=float, factor=1, type=str):
    """
    Calculates all uncertainties of the data.
    This does not include error propagation as that is a different type of uncertainty. Please execute error_propagation for that.
    ===========================
    
    Args:
    data: numpy array
        All the data of one size taken of which the uncertainty should be calculated.
    type_b: float (optional)
        Display increment for type b uncertainty (distance between two neighbouring scale steps)
    method: str ('analog' or 'digital') (optional)
        Method of measurement
    percentage: indicated acuracy. CAUTION: give as decimal (optional)
            Ex: 2.0% please enter 0.02
    digit: int (optional)
        increasment by digits (given by producer).
    scale_end: float (optional)
        Only needed with analog device. End of scale.
    factor: int (optional)
        Scale of expansion of uncertainty
    type: str (optional)
        'linear' or 'gaussian' for the respective type of error propagation.
    ===========================
    
    Return:
    array or float.
    Combined uncertainty of all values.
    """

    unca = type_a(data)
    uncb = type_b(b, method)
    device = device_acuracy(data, method, percentage, digit,scale_end)
    comb1 = combined_unc([unca,uncb,device])
    expand = expanded_unc(comb1, factor)
    return expand