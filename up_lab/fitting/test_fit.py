#from basic_functions import linear_fit
#from fitting.fit import least_square_method_fit
import matplotlib.pyplot as plt


X = [1, 2, 3, 4, 5]
Y = [2, 3, 5, 4, 6]

#print(least_square_method_fit(X,Y,weighted=True))
from basic_functions import function_availibility
print("Works so far")
func_avail = function_availibility()
print(func_avail(X,2,3))
