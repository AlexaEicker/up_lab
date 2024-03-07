import numpy as np
import pandas as pd

def type_change(values, to):
    '''
    Change of dictionary and list to numpy - Array or the other way around.
    ===========

    Args: 
    values: Array - like. Dictionary, list or numpy - Array.
    to: type. numpy - Array or list.
    =====================

    Return:
    values: Transformed to numpy - Array or list, depending of 'to'.
    '''

    #Defining test variable for input rerun
    key_test =True

    if type(values)==to:
        pass
    else:
    #Transformation of all possible given types
        if type(values)==dict:
            while key_test:
                #Requests one particular key to transform right numbers.
                key = input("Enter key (name) of the value needed for this calculation:")
                #Checks wheter input is valid. If not, requests new input and gives all possible keys
                key_test = key not in values
                if key_test ==True:
                    print("Given name is not in your dictionary.")
                    print("Here are all possible names: \n", values.keys())
                else:
                    values = np.array(values[key])
            if to ==list:
                values = values.tolist()
            elif to ==np.array:
                pass
            else:
                raise ValueError("Wrong type for 'to' variable. Please check. Possible values: \n np.array and list")
            
        elif type(values)==list:
            if to==np.array:
                values = np.array(values)
            elif to==list:
                pass
            else:
                raise ValueError("Wrong type for 'to' variable. Please check. Possible values: \n np.array and list")
            
        elif type(values)==np.array:
            if to ==list:
                values = values.tolist()
            elif to ==np.array:
                pass
            else:
                raise ValueError("Wrong type for 'to' variable. Please check. Possible values: \n np.array and list")
        else:
            raise TypeError("Unexpected type. Please change your variable type to\n a numpy - Array, list or dictionary.")
    return values




def statistical_analysis(data):
    '''
    Calculates the basic statistical measures of data distribution.
    
    Calculates mean, median, mode, standard deviation, variance and range. 
    '''

    mean = np.mean(data)
    median = np.median(data)
    
    #Calculation of mode of dataset ()


def hypothesis_test():
    '''
    Tests data on common hypothesises by statistical test.

    t - Test, chi**2 - Test, analysis of variance (ANOVA), regression analysis, correlation analysis.
    '''


def polation():
    '''
    Calculation of interpolation and extrapolation.
    
    Interpolation: intermediate values between measured data points.
    Extrapolation: Estimation of values beyond range of measured data.'''


def least_squares_regression(X, Y):
    """
    Calculate linear regression using the method of least squares.

    Parameters:
        X (array-like): Independent variable data (e.g., list, NumPy array).
        Y (array-like): Dependent variable data corresponding to X.

    Returns:
        tuple: A tuple containing the slope (m) and intercept (b) of the regression line.
    """

    X = type_change(X,np.array)
    Y = type_change(Y,np.array)
    n = len(X)

    sum_X = np.sum(X)
    sum_Y = np.sum(Y)
    X_squared = X**2
    sum_X_squared = np.sum(X_squared)
    sum_XY = np.sum(X * Y)

    # Calculate slope (m) and intercept (b) using least squares formulas
    m = (n * sum_XY - sum_X * sum_Y) / (n * sum_X_squared - sum_X**2)
    b = (sum_Y - m * sum_X) / n

    return m, b
