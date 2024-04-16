import numpy as np
#from uncertainty import type_a, type_b, combined_unc, device_acuracy, error_propagation
#from derivate import derivatives
#from basic_calc import least_squares_regression, type_change

string='1324.56'
eins=False
zwei=False
for char in string:
    if char=='2':
        zwei=True
        if eins:
            print('Eins kam schon, jetzt kommt zwei')
    elif char=='1':
        eins=True

if '1' and '2' in string:
    print("Es gibt ne 1 und ne 2")

random_measurements = [np.random.random() for _ in range(4)]
random_int = np.random.randint(1,100)
print("Random measurement values: ",'\n', random_measurements)
print(len(random_measurements))
#print(type_a(random_measurements))
#uncb = type_b(0.04,'digital')
#print(uncb)

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
print(error_propagation(random_measurements, 'gaussian'))


X = [1, 2, 3, 4, 5]
Y = [2, 3, 5, 4, 6]
dic = {'X': [1, 2, 3, 4, 5], 'Y':[2, 3, 5, 4, 6] }

#print(least_squares_regression(X,Y))

#print(type_change(dic,list))

#print(type_a(dic))

def calculate_mode(data):
    frequency_dict = {}
    
    # Count occurrences of each element in the list
    for item in data:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    
    # Find the element(s) with the maximum count
    max_frequency = max(frequency_dict.values())
    modes = [key for key, value in frequency_dict.items() if value == max_frequency]
    
    if len(modes) == 1:
        return modes[0]  # Single mode
    else:
        return modes  # Multiple modes

# Example usage:
data = [1, 2, 3, 3, 4, 5,  5, 6]
print("Mode:", calculate_mode(data))




#digit access for device_accuracy 
#This is bullshit
def digit_access(number, digit):
    """Recreates number only at digits point"""

    number_str = str(number)
    important_num = number_str[-digit]
    if important_num=='.':
        important_num = number_str[-(digit+1)]
    print(important_num)
    return_num = int
    dotpos = int
    dotposfound = False
    i =0
    while not dotposfound:
        print(i)
        for char in number_str:
            if char=='.':
                dotpos = i
            i=i+1
