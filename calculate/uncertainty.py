import numpy as np
from scipy.stats import t
from .derivate import derivatives as derivate_derivatives
from .basic_calc import type_change

def type_a(values):
    ''' Calculates type A uncertainty

    Type A uncertainty according to ISO/IEC Guide 98-3
    
    Args:
    distribution: String, distribution of measurements. Default: Gauss
    values: measured values taken in the experiment; numpy-array

    '''

    values = type_change(values,np.array)
    N=len(values)
    values_mean=np.mean(values)
    values_sum=sum((values-values_mean)**2)
    unc_typea= (1/(N-1)*values_sum)**(1/2)/(N**(1/2))

    # Calculate student factor for a confidence level of 68.3%  
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
    method: 'digital' or 'analog' depending of the type of measuring
    
    '''

    if method=='digital':
        unc_typeb = b/(2*3**(1/2))
    elif method=='analog':
        unc_typeb= b/(2*6**(1/2))
    else:
        print("Your method could not be determind. Please type 'digital' or 'analog'")
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
        increasment by digits (given by producer). Type: Integer.
    scale_end: float.
        Only needed with analog device. End of scale. Type: Float.
    ======================

    Return:
    
    '''

    values = type_change(values, np.array)
    if method=='analog':
        unc_device = percentage * scale_end
    elif method=='digital':
        unc_device = np.zeros(len(values))
        for i in range(len(values)):
            number = values[i]
            if type(number)==int:
                digit =1
            else:
                number_list = str(number).split('.')
                digit = 1 * 10**(-len(number_list[1]))
                
            unc_device = values[i]*percentage + digit
    print(type(unc_device))
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

def error_propagation(uncertainties,typ=str):
    '''
    Calculates the uncertainty according to linear and gaussian law of propagation of measurement uncertainties.
    This is needed when the variable is defined by the taken measurement variables. 
    Ex: s = v*t. v and t are measured. This calculation is necessary, if you are looking for s.
    ===========================

    Args:
    uncertainties: Array - like or float
        Uncertainties of all variables needed to calculate the uncertainty of variable. 
        If a variable is given or doesn't have an uncertainty, add '0' to your list.
    typ: str.
        'linear' or 'gaussian' for the respective type of error propagation.
    ==========

    Return:
    float. 
    '''
    
    uncertainties = type_change(uncertainties, list)
    derivate = derivate_derivatives()
    list_multiplies = []
    if len(derivate)<len(uncertainties):
        raise ValueError("You entered LESS variables to derivate to than you have uncertainties. This does not work. Please check your formula, your variables and the uncertainties you entered.")
    elif len(derivate)>len(uncertainties):
        raise ValueError("You entered MORE variables to derivate to than you have uncertainties. This does not work. Please check your formula, your variables and the uncertainties you entered.")
    else:
        if typ=='linear':
            for i in range(0,len(derivate)):
                list_multiplies.append(derivate[i]*uncertainties[i])
        elif typ=='gaussian':
            for i in range(0,len(derivate)):
                list_multiplies.append((derivate[i]*uncertainties[i])**2)
        else:
            raise ValueError("Wrong type. Please type 'linear' or 'gaussian'.")
        print(list_multiplies)
        error_propagation = sum(list_multiplies)
    return error_propagation


