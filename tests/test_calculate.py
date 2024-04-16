#from up_lab.calculate.uncertainty import error_propagation
import numpy as np
import sympy as sp
idata = np.array([0.1,0.17,0.12,0.09,0.12])
udata = np.array([1,2,3,4,5])
k=0
for i in udata:
    k += i
    print(k)
alldata = [udata, idata]
print(len(alldata[0]))

variables = ('x,t').split(',')
syms = sp.symbols(variables)
print(syms, type(syms[0]))

for k in range(0, len(alldata[0])):
    print(k)
