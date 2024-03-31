import numpy as np
import pandas as pd
from scipy import stats


def type_change(values, to):
    '''
    Change of dictionary and list to numpy - Array or the other way around.
    ===========

    Args: 
    values: Array - like. Dictionary, list or numpy - Array.
    to: type. numpy - Array or list.
        Type np.array for numpy array or list for list.
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
                if key_test:
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



def statistical_analysis(data, dict_out=True):
    '''
    Calculates the basic statistical measures of data distribution.
    
    Calculates mean, median, mode, standard deviation, variance and range. 
    ===================================

    Args:
    data: array_like
        Data used for statistical analysis
    dict_out: bool
        Default True. 
        Should output be a dictionary with names and values of all measures calculated?
        If False: output is every measure as seperate values
    ====================================

    Return:
    dict or floats and arrays 
    ===========================
    Mean: Average by summing all values and dividing by total number of values.
    Median: Middle value of sorted data set.
    Mode: Most frequent value in data set.
    Standard deviation: Square root of sum over squared difference between value and mean. Low -> values are close to mean, high -> values are spread out. 
    Variance: Difference from mean. Calculated by average of squared differences between value and mean.
    Range: Difference between largest and smallest value.
    '''

    data= type_change(data, np.array)
    #Calculation of measures provided by numpy 
    #mean, median, range
    mean = np.mean(data)
    median = np.median(data)
    #Calculation of range (maximum value - minimum value)
    range = max(data)-min(data)
    standard_deviation = np.std(data)
    variance = np.var(data)
    
    
    #Calculation of mode of dataset (most common value)
    frequency_dict = {}
    
    # Count occurrences of each element in the list
    for item in data:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    max_frequency = max(frequency_dict.values())
    modes = [key for key, value in frequency_dict.items() if value == max_frequency]
    
    if len(modes) == 1:
        modes= modes[0] 
    else:
        pass
    
    if dict_out:
        return_dict = {'Mean': mean, 'Median': median,'Mode':modes, 'Standard deviation':standard_deviation, 'Variance':variance, 'Range':range}
        return return_dict
    else:
        return mean,median, modes, standard_deviation,variance,range
    





def hypothesis_test(*data):
    '''
    Tests data on common hypothesises by statistical test.

    t - Test, chi**2 - Test, analysis of variance (ANOVA), linear regression analysis, Pearson correlation analysis.
    =============================

    Args:
    *data: array_like or array of array_likes
        All the data you have a hypothesis for. Send entire dataset.
        Ex: Hypothesis: y=mx+b (m,b const) 
        Send x,y as arrays to the function to test.
    ==========================

    Return:
    Depending on amount of data arrays. Results of all possible hypothesis with the dataset.
    If len(data)==1:
    Chi**2 test: statistic, p value , degrees of freedom

    If len(data)==2:
    ANOVA: F statistic, p value
    t Test: statistic, p value
    linear regression: r value, p value
    Correlation analysis: correlation coefficent, p value

    Else:
    ANOVA: F statistic, p value
    =============================

    For explanation of tests (function) see help for:
    t - Test: scipy.stats.ttest_ind()
    chi**2 - Test: scipy.stats.chi2_contingency()
    ANOVA: scipy.stats.f_oneway()
    Linear regression analysis: scipy.stats.linregress()
    Pearson correlation analysis: scipy.stats.pearsonr()
    '''
    
    #Assigns each test to its conditions
    if len(data)==1:
        chi2_statistic, p_value_chi, degrees_of_freedom_chi, _ = stats.chi2_contingency(data)
        return chi2_statistic, p_value_chi, degrees_of_freedom_chi
    else:
        F_statistic_anova, p_value_anova = stats.f_oneway(*data)
        if len(data)==2:
            t_stat, p_value_t = stats.ttest_ind(data[0],data[1])
            _,_, r_value_lin, p_value_lin,_ = stats.linregress(data[0], data[1])
            correlation_coefficient, p_value_correlation = stats.pearsonr(data[0],data[1])
            return F_statistic_anova, p_value_anova, t_stat, p_value_t, r_value_lin, p_value_lin, correlation_coefficient, p_value_correlation

        else:
            return F_statistic_anova,p_value_anova


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
