import matplotlib.pyplot as plt
from fitting.fit import fit_ls
import numpy as np
 

def array_plot(xdata,ydata, xerr=None, yerr=None, xlabel='x Axis',ylabel='y Axis', weighted=False, function=None,data_label='Data',function_label=str,title='Title', fmt_data='bx',fmt_fit='r',xscale = 'cartesian', yscale='cartesian',kwargs_func =dict,data=None, **kwargs):
    """Plots data in numpy - arrays with errorbars as well as 1 choosen fit.
    =====================

    Args:
    xdata: array_like
    ydata: array_like

    _The following arguments are optional_
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
        Fit function 
    data_label: str
    function_label: str
    title: str
        Default: Title
        Title of plot
    fmt_data: str
        Default: bx (blue, x-Marker)
        Format of data plot
    fmt_fit: str
        Default: r (red)
        Format of fit plot
    xscale: str
        Default: linear
        Type of xscale. The supported strings are `'linear'`, `'log'`, `symlog` and `logit`. See explanation below
    yscale: str
        Default: linear
        Type of yscale. The supported strings are `'linear'`, `'log'`, `symlog` and `logit`. See explanation below.
    kwargs_func: dict
        dictionary of kwargs for plot of fit function. See matplotlib.pyplot.plot for available kwargs.
    data: indexable object
        An object with labelled data. If given, provide the label names to plot in x,y, xerr and yerr.
    **kwarg:
        See matplotlib.pyplot.plot for available options to pass.
    ==============================

    Return:
    fitting parameter: numpy Array
    uncertainty of fitting parameters: numpy Array
    residuals: numpy Array
    reduced chi**2: float
    Opens plot.
    ======================

    Scale types:
    linear: equidistant steps. Usually used for cartesian coordinates.
    log: logarithmic scale.  Care is taken to only plot positive values.
    symlog: symmetrical logarithmic scale. Logarithmic in both directions from the origin but with linear range around zero.
    logit: logit scale. This scale is similar to a log scale close to zero and to one, and almost linear around 0.5. It maps the interval ]0, 1[ onto ]-infty, +infty[.
    """

    return_val = []
    plt.errorbar(xdata,ydata,yerr=yerr,xerr=xerr, fmt=fmt_data, label=data_label,  capsize=1,**kwargs)
    if function==None:
        return_val=[]
    else:
        #x values for plot of function
        if len(xdata)<=250:
            num_plot = 500
        elif len(xdata)<=500:
            num_plot = 2*len(xdata)
        else:
            num_plot = 1000
        xplot = np.linspace(min(xdata),max(xdata), num=num_plot)
        if not function_label:
            function_label ="Fit of " +function.__name__
        params, params_cov, function_fit, residuals,reduced_chisquare = fit_ls(xdata,ydata,function,weighted,yerr)
        plt.plot(xplot, function(xdata, *params), fmt=fmt_fit, label=function_label, **kwargs_func)
        return_val = [params, params_cov, residuals, reduced_chisquare]
    
    plt.grid(True)
    plt.legend()
    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    return *return_val,
