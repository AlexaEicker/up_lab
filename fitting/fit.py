import numpy as np
import matplotlib as pl
import pandas as pd
from scipy.optimize import curve_fit
from .basic_functions import function_availibility

#np.polyfit()

def least_square_method_fit(xdata, ydata, function=None, weighted=False, uncertainty=None):
    '''
    Fits function to data using least square method.
    =========================
    
    Args:
    xdata: array_like
        Independnent variable (Measured).
    ydata: array_like
        Dependent variable.
    function: callable, optional
        Default None to choose from selection of basic functions.
    weighted: bool, optional
        Should fit be weighted? Yes = True, No = False.
        Default: False.
    uncertainty: array_like, optional
        Uncertainty in ydata!
        Only neccessary for weighted least square fit.
    ============
    
    Return:
    4 numpy - Arrays.
        Fitted parameters of function, covariance of fitted parameters, f(x) for all xdata, and residuals.
    float:
        reduced chi - square. Function is a good approximation if reduced chi - square is approximatly 1.
    '''

    if function is None:
        function = function_availibility()
    else:
        pass
    
    if not weighted:
        params, params_covariance = curve_fit(function, xdata,ydata)
    else:
        params, params_covariance = curve_fit(function, xdata, ydata, sigma=uncertainty, absolute_sigma=True)

    params_cov = np.array
    for i in range(len(params)):
        params_cov[i] = (params_covariance[i][i])**(1/2)

    if len(params)==2:
        f_x = function(xdata,params[0], params[1])
        residuals = f_x-ydata
    elif len(params)==3:
        f_x = function(xdata, params[0], params[1], params[2])
        residuals = f_x- ydata
    elif len(params)==4:
        f_x = function(xdata, params[0], params[1], params[2], params[3])
        residuals =f_x-ydata
    elif len(params)==5:
        f_x = function(xdata, params[0], params[1], params[2], params[3], params[4])
        residuals = f_x-ydata
    else:
        raise ValueError("Something went wrong :(")
    
    #Reduced chi square
    rcs = reduced_chi_square(xdata, ydata,uncertainty,function, *params)
    return params,params_cov,f_x, residuals, rcs

def chi_square(residuals, yerr):
    '''
    Calculates chi - square.
    chi - square = sum(1/yerr**2 * residuals**2)
    =============
    
    Args:
    residuals: array_like
    yerr: array_like
    ==========
    
    Return:
    float.'''

    chi_square = sum(1/yerr**2 * residuals**2)
    return chi_square

def reduced_chi_square(xdata, ydata, yerr, func, *args):
    '''
    Calculates reduced chi square.
    ================
    
    Args:
    xdata: array_like
    ydata: array_like
    yerr: array_like
    func: callable
    *args: array_like
        Arguments choosen to fit func to data.
    =========================
    
    Return:
    float
    '''

    reduced_chi_square = 1/(len(xdata)-len(args))*np.sum((func(xdata, *args)-ydata)**2/yerr**2)
    return reduced_chi_square




