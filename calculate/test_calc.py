import numpy as np
from uncertainty import type_a, type_b, combined_unc, device_acuracy, error_propagation
from derivate import derivatives
from basic_calc import least_squares_regression, type_change

random_measurements = [np.random.random() for _ in range(4)]
random_int = np.random.randint(1,100)
print("Random measurement values: ",'\n', random_measurements)
print(len(random_measurements))
#print(type_a(random_measurements))
#uncb = type_b(0.04,'digital')
#print(uncb)

#print("Combined ",combined_unc(random_measurements,0.04,'analog'))
#conv = str(random_measurements[0])
#decimal = str(random_measurements[0]%1).split('.')
#decimal_len = len(decimal[1])
#print(conv, '\n', decimal)
#print("['0'", 1*10**(-decimal_len))
#print(len(conv), 'len dec', decimal_len)

#print(str(random_int).split('.'))
#if type(random_int) == int:
   # print('HALLÖCHEN')
#print(len(random_measurements))
#unc_pl = sum(x**2 for x in random_measurements)
#print(0.375456323+unc_pl)
#uncertainties = [type_b(0.036,'digital'), type_a(random_measurements), device_acuracy(random_measurements,'digital',0.03,random_int)]
#print(uncertainties)
#print(combined_unc(uncertainties))
#print(combined_unc(random_measurements,random_int,'analog',device_acuracy(random_measurements,'analog',0.0046,random_int,20)))


#Derivative test
#print(derivatives())
#print(error_propagation(random_measurements, 'gaussian'))


X = [1, 2, 3, 4, 5]
Y = [2, 3, 5, 4, 6]
dic = {'X': [1, 2, 3, 4, 5], 'Y':[2, 3, 5, 4, 6] }

#print(least_squares_regression(X,Y))

#print(type_change(dic,list))

#print(type_a(dic))
