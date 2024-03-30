import matplotlib.pyplot as plt
#from fitting.fit import least_square_method_fit
import numpy as np

#TODO: import of least_square_method_fit!

def array_plot(xdata,ydata, xerr=[0], yerr=[0], xlabel='x Axis',ylabel='y Axis', weighted=False, function=None,data_label='Data',function_label=str,title='Title', fmt_data='bx',fmt_fit='r',**kwargs):
    """Plots data in numpy - arrays with errorbars as well as 1 choosen fit.
    =====================

    Args:
    xdata: array_like
    ydata: array_like
    xerr: array_like
    yerr: array_like
    xlabel: str
        Default: x Axis
        Please mention unit of size
    ylabel: str
        Default: y Axis
        Please mention unit of size
    weighted: bool
    function: callable
    data_label: str
    function_label: str
    title: str
        Default: Title
        Title of plot
    fmt: str
        Default: bx (blue, x-Marker)
    
    ==============================

    Return:
    residuals: numpy Array
    reduced chi**2: float
    ======================
    Opens plot (maybe??)
    """

    #List of return values
    return_val = []
    #x values for plot of function
    if len(xdata)<=250:
        num_plot = 500
    elif len(xdata)<=500:
        num_plot = 2*len(xdata)
    else:
        num_plot = 1000
    xplot = np.linspace(min(xdata),max(xdata), num=num_plot)

    plt.errorbar(xdata,ydata,yerr=yerr,xerr=xerr, fmt=fmt_data, capsize=1,**kwargs)
    if function==None:
        return_val=[]
    else:
        #params, params_cov, function_fit, residuals,reduced_chisquare = least_square_method_fit(xdata,ydata,function,weighted,yerr)
        #plt.plot(xplot, function(xdata, *params), fmt=fmt_fit, label=function_label)
        #return_val = [params_cov, residuals, reduced_chisquare]
        pass
    
    plt.grid(True)
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    return *return_val,



#Test 
#Example data
xdata = [123,345,340,346,645,234,356]
ydata = [2,4,5,9,3,6,3]
def linfunc(x,a,b):
    return a*x+b
#Test array_plot
array_plot(xdata, ydata,yerr=0.4,weighted=True)