import numpy as np
import matplotlib as plt
import pandas as pd
from scipy.optimize import curve_fit

#Definition of typical fit functions

def linear_function(x,a,b):
    return a*x+b

def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

def cubic_function(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

def quartic_function(x, a, b, c, d, e):
    return a * x**4 + b * x**3 + c * x**2 + d * x + e

def exponential_function(x, a, b):
    return a * np.exp(b * x)

def logarithmic_function(x, a, b):
    return a * np.log(x) + b

def sigmoid_function(x, a, b):
    return a / (1 + np.exp(-b * x))

def power_law_function(x, a, b):
    return a * x**b

def gaussian_function(x, a, b, c):
    return a * np.exp(-((x - b)**2) / (2 * c**2))

def sine_function(x, a, b):
    return a * np.sin(b * x)

def cosine_function(x, a, b):
    return a * np.cos(b * x)

def tangent_function(x, a, b):
    return a * np.tan(b * x)


#
#When adding a function to the dictionary, you HAVE to add its name (and mathematical expression (optional)) to function_name_dict.
#Otherwise, user cannot choose the new function
#
function_dict = {
    'Linear function': linear_function, 
    'Quadratic funtion' : quadratic_function,
    'Cubic function': cubic_function,
    'Quartic function':quartic_function,
    'Exponential function':exponential_function,
    'Sigmoid function':sigmoid_function,
    'Power law function':power_law_function,
    'Gaussian function':gaussian_function,
    'Sine function':sine_function,
    'Cosine function':cosine_function,
    'Tangent function':tangent_function
}

#Adds mathematical expression to function name. When adding function to function_dict please update function_name_dict as well.
function_name_dict = {
    'Linear function': 'ax+b',
    'Quadratic function': 'ax**2+bx+c',
    'Cubic function': 'ax**3+bx**2+cx+d',
    'Quartic function': 'ax**4+bx**3+cx**2+dx+e',
    'Exponential function': 'ae**(bx)',
    'Sigmoid function': 'a/1+e**(-bx)',
    'Power law function': 'ax**b',
    'Gaussian function': 'ae**(-(x-b)**2/2c**2)',
    'Sine function': 'a sin(bx)',
    'Cosine function' :'a cos(bx)',
    'Tangent function':'a tan(bx)'
}



def function_availibility(formulaout=False):
        """
        Choose from selection of basic functions.
        Returns python function that was chosen during this function.

        Arg:
        formulaout: bool
            Default: False. If True, output is a string.
        """

        print("Possible functions to choose from: \n")
        #neater output of dictionary
        for key,value in function_name_dict.items():
            print(key,': ',value)
        function_keys = input("Enter fitting function name as given above:")
        key_test = function_keys not in function_dict
        if key_test:
            print("Function not defined. Please write your own function.")
            function_avail=None
        else:
            if not formulaout:
                function_avail = function_dict[function_keys]
                print("Choosen function:\n", function_avail.__name__)
            else:
                function_avail = function_name_dict[function_keys]
        return function_avail





def fit_ls(xdata, ydata, function=None,yerr=0, weighted=False):
    """
    Fits function to data using least square method.
    =========================
    
    Args:
    xdata: array_like
        Independnent variable (Measured).
    ydata: array_like
        Dependent variable.
    function: callable, optional
        Default None to choose from selection of basic functions.
    yerr: array_like, optional
        Uncertainty in ydata.
        Necessary for weighted fit (not representative otherwise) and reduced chi^2.
    weighted: bool, optional
        Should fit be weighted? Yes = True, No = False.
        Default: False.
    ============
    
    Return:
    4 numpy - Arrays.
        Fitted parameters of function, covariance of fitted parameters, f(x) for all xdata, and residuals.
    float:
        reduced chi - square. Function is a good approximation if reduced chi - square is approximatly 1.
    ====================================

    For further help and documentation see: scipy.optimize.curve_fit
    """

    xdata = np.array(xdata)
    ydata = np.array(ydata)
    if function is None:
        function = function_availibility()
    
    if not weighted:
        params, params_covariance = curve_fit(function, xdata,ydata)
    else:
        params, params_covariance = curve_fit(function, xdata, ydata, sigma=yerr, absolute_sigma=True)

    #Covariance of all parameters of function (sqrt of values on main diagonal of params_covariance matrix)
    params_cov = np.array([])
    for i in range(len(params)):
        params_cov = np.append(params_cov,(params_covariance[i][i])**(1/2))

    f_xdata = function(xdata, *params)
    residuals = f_xdata - ydata

    rcs = reduced_chi_square(xdata, ydata,yerr,function, *params)
    return params,params_cov,f_xdata, residuals, rcs


def chi_square(residuals, yerr):
    """
    Calculates chi - square.
    chi - square = sum(1/yerr**2 * residuals**2)
    =============
    
    Args:
    residuals: array_like
    yerr: array_like
    ==========
    
    Return:
    float.
    ==========

    Large values indicate a greater discrepance between observed and fitted frequencies.
    When value exceedes a certain value, there is no association between the values.
    """

    chi_square = sum(1/yerr**2 * residuals**2)
    return chi_square

def reduced_chi_square(xdata, ydata, yerr, function, *args):
    """
    Calculates reduced chi square.
    ================
    
    Args:
    xdata: array_like
    ydata: array_like
    yerr: array_like
    function: callable
    *args: array_like
        Arguments choosen to fit func to data.
    =========================
    
    Return:
    float
    """

    reduced_chi_square = 1/(len(xdata)-len(args))*np.sum((function(xdata, *args)-ydata)**2/yerr**2)
    return reduced_chi_square
