import numpy as np
import matplotlib as pl
import pandas as pd
from scipy.optimize import curve_fit
from basic_functions import function_availibility


#TODO: import of functions and use of function if loop

def least_square_method_fit(xdata, ydata, function=None, weighted=False, uncertainty=0):
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
    ====================================

    For further help and documentation see: scipy.optimize.curve_fit
    """

    xdata = np.array(xdata)
    ydata = np.array(ydata)

    #if function is None:
       # function = function_availibility()
    #else:
       # pass
    
    if not weighted:
        params, params_covariance = curve_fit(function, xdata,ydata)
    else:
        params, params_covariance = curve_fit(function, xdata, ydata, sigma=uncertainty, absolute_sigma=True)

    #Covariance of all parameters of function (sqrt of values on main diagonal of params_covariance matrix)
    params_cov = np.array
    for i in range(len(params)):
        params_cov = np.append(params_cov,(params_covariance[i][i])**(1/2))

    #function values for all x data and residuals
    f_xdata = function(xdata, *params)
    residuals = f_xdata - ydata
    
    #Reduced chi square
    rcs = reduced_chi_square(xdata, ydata,uncertainty,function, *params)
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



#TEST LEAST_SQUARE_FIT
if __name__ =="__main__":
    X = np.array([1, 2, 3, 4, 5,6])
    Y = np.array([2, 3, 5, 4, 6,8])
    def funktion_hoer_mir_auf(x,a,b):
        return b*x+a
    print(least_square_method_fit(X,Y,funktion_hoer_mir_auf))
