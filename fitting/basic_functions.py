import numpy as np
import matplotlib.pyplot as plt

def linear_fit(x,a,b):
    return b*x+a

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

function_dict = {
    'Linear function': linear_fit, 
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
    'Linear function': 'ax +b',
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

def function_availibility():
        """
        Choose from selection of basic functions.
        """

        print("Possible functions to choose from: \n")
        print(function_name_dict.items())
        function_keys = input("Enter fitting function as given above:")
        key_test = function_keys not in function_dict
        if key_test ==True:
            print("Function not defined. Please write your own function.")
        else:
            function_avail = function_dict[function_keys]
        print("Choosen function:\n", function_avail)
        return function_avail
    


