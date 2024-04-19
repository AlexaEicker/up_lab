import numpy as np
#from uncertainty import type_a, type_b, combined_unc, device_acuracy, error_propagation
#from derivate import derivatives
#from basic_calc import least_squares_regression, type_change
if __name__ =="__main__":
    #from basic_calc import type_change
    #numpydata = np.array([1,2,3,4])
    #print('Anfang: ',numpydata, type(numpydata))
    #listdata = type_change(numpydata, list)
    #print('Nach Umwandlung: ',listdata, type(listdata))
#
    #listdata = [1,2,3,4]
    #print('Anfang: ',listdata , type(listdata))
    #numpydata = type_change(listdata, np.array)
    #print('Nach Umwandlung: ', numpydata, type(numpydata))
#
    #dictdata = {'Data':[1,2,3,4], 'Extra': 'Hello World'}
    #print('Anfang: ', dictdata, type(dictdata))
    #numpydata= type_change(dictdata,np.array)
    #print('Nach Umwandlung: ',numpydata , type(numpydata))
#
    #dictdata = {'Data':[1,2,3,4], 'Extra': 'Hello World'}
    #print('Anfang: ',dictdata , type(dictdata))
    #listdata= type_change(dictdata,list)
    #print('Nach Umwandlung: ',listdata , type(listdata))

    #from basic_calc import statistical_analysis
    #unimodedata = [2,3,4,4,5,6]
    #unimodedict = statistical_analysis(unimodedata)
    #print(unimodedata,'\n', unimodedict)
    #bimodedata = [2,2,3,4,5,5,6]
    #bimean, bimedian,bimode, bistandard, bivar, birange = statistical_analysis(bimodedata, dict_out=False)
    #print(bimodedata, '\n Out: Mean: {0}, Median: {1}, Mode: {2}, Standard deviation: {3:.3f}, Variance: {4:.3f}, Range: {5}'.format(bimean, bimedian, bimode, bistandard,bivar,birange))

    #from basic_calc import hypothesis_test
    #hypx = [1,2,3,4,5]
    #hypy = [1,4,8.4,18.2,30]
    #returnhyp = hypothesis_test(hypx,hypy)
    #print(returnhyp)
    #returnhyp = hypothesis_test(hypx)
    #print(returnhyp)

    #import conversion
    #C = 100
    #K = 373.15
    #F = 212
    #inch = 1968.5039370078741
    #ft = 164.04199475065616
    #mi = 0.0310685596118667
    #meter = 50
    #kg = np.array([0.1,0.2,0.3])
    #lbs = np.array([0.2205,0.4409,0.661])
    #oz = np.array([3.527,7.055,10.582])
    #min = 10
    #sec = 600
    #h = 1/6
    #
    ##Convert
    #print("Temperature \n","K to C: ",conversion.K_to_C(K), "C to K: ",conversion.C_to_K(C), "F to K: ", conversion.F_to_K(F))
    #print("Length \n", "In to m: ", conversion.in_to_m(inch), "M to in: ", conversion.m_to_in(meter), "Ft to m: ", conversion.ft_to_m(ft))
    #print("M to ft: ", conversion.m_to_ft(meter), "Miles to m: ", conversion.mi_to_m(mi), "M to miles: ", conversion.m_to_mi(meter))
    #print("Mass \n", "Oz to kg: ", conversion.oz_to_kg(oz), "Kg to oz: ", conversion.kg_to_oz(kg), "Lbs to kg: ", conversion.lbs_to_kg(lbs))
    #print("Kg to lbs: ", conversion.kg_to_lbs(kg))
    #print("Time \n", "Min to sec: ", conversion.min_to_sec(min), "Sec to min: ", conversion.sec_to_min(sec), "h to min: ", conversion.h_to_min(h))
    #print("min to h: ", conversion.min_to_h(min), "Sec to h: ", conversion.sec_to_h(sec), "h to sec: ", conversion.h_to_sec(h))

    from uncertainty import type_a, type_b
    tenperiods = [11.41,11.91,11.87]
    print(type_a(tenperiods))
    #Step on measuring device
    a=0.001
    print("Digital uncertainty:",type_b(a,'digital'))
    print("Analog:", type_b(a,'analog'))
    print("Wrong method:", type_b(a,'Analog'))





















#string='1324.56'
#eins=False
#zwei=False
#for char in string:
#    if char=='2':
#        zwei=True
#        if eins:
#            print('Eins kam schon, jetzt kommt zwei')
#    elif char=='1':
#        eins=True
#
#if '1' and '2' in string:
#    print("Es gibt ne 1 und ne 2")
#
#random_measurements = [np.random.random() for _ in range(4)]
#random_int = np.random.randint(1,100)
#print("Random measurement values: ",'\n', random_measurements)
#print(len(random_measurements))
##print(type_a(random_measurements))
##uncb = type_b(0.04,'digital')
##print(uncb)
#
##conv = str(random_measurements[0])
##decimal = str(random_measurements[0]%1).split('.')
##decimal_len = len(decimal[1])
##print(conv, '\n', decimal)
##print("['0'", 1*10**(-decimal_len))
##print(len(conv), 'len dec', decimal_len)
#
##print(str(random_int).split('.'))
##if type(random_int) == int:
#   # print('HALLÖCHEN')
##print(len(random_measurements))
##unc_pl = sum(x**2 for x in random_measurements)
##print(0.375456323+unc_pl)
##uncertainties = [type_b(0.036,'digital'), type_a(random_measurements), device_acuracy(random_measurements,'digital',0.03,random_int)]
##print(uncertainties)
##print(combined_unc(uncertainties))
##print(combined_unc(random_measurements,random_int,'analog',device_acuracy(random_measurements,'analog',0.0046,random_int,20)))
#
#
##Derivative test
##print(derivatives())
##print(error_propagation(random_measurements, 'gaussian'))
#
#
#X = [1, 2, 3, 4, 5]
#Y = [2, 3, 5, 4, 6]
#dic = {'X': [1, 2, 3, 4, 5], 'Y':[2, 3, 5, 4, 6] }
#
##print(least_squares_regression(X,Y))
#
##print(type_change(dic,list))
#
##print(type_a(dic))
#
#def calculate_mode(data):
#    frequency_dict = {}
#    
#    # Count occurrences of each element in the list
#    for item in data:
#        if item in frequency_dict:
#            frequency_dict[item] += 1
#        else:
#            frequency_dict[item] = 1
#    
#    # Find the element(s) with the maximum count
#    max_frequency = max(frequency_dict.values())
#    modes = [key for key, value in frequency_dict.items() if value == max_frequency]
#    
#    if len(modes) == 1:
#        return modes[0]  # Single mode
#    else:
#        return modes  # Multiple modes
#
## Example usage:
#data = [1, 2, 3, 3, 4, 5,  5, 6]
#print("Mode:", calculate_mode(data))
#
#
#
#
##digit access for device_accuracy 
##This is bullshit
#def digit_access(number, digit):
#    """Recreates number only at digits point"""
#
#    number_str = str(number)
#    important_num = number_str[-digit]
#    if important_num=='.':
#        important_num = number_str[-(digit+1)]
#    print(important_num)
#    return_num = int
#    dotpos = int
#    dotposfound = False
#    i =0
#    while not dotposfound:
#        print(i)
#        for char in number_str:
#            if char=='.':
#                dotpos = i
#            i=i+1
#
#
#
##from up_lab.calculate.uncertainty import error_propagation
#import numpy as np
#import sympy as sp
#idata = np.array([0.1,0.17,0.12,0.09,0.12])
#udata = np.array([1,2,3,4,5])
#k=0
#for i in udata:
#    k += i
#    print(k)
#alldata = [udata, idata]
#print(len(alldata[0]))
#
#variables = ('x,t').split(',')
#syms = sp.symbols(variables)
#print(syms, type(syms[0]))
#
#for k in range(0, len(alldata[0])):
#    print(k)