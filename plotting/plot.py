import matplotlib.pyplot as plt
from fitting.fit import least_square_method_fit


def array_plot(xdata,ydata, xerr, yerr, weighted=False, function=None,data_label='Data',function_label=str,title='Title', fmt_data='bx',fmt_fit='r', *axis_label ):
    """
    Plots data with errorbars as well as 1 choosen fit.
    =====================

    Args:
    xdata: array_like
    ydata: array_like
    xerr: array_like
    yerr: array_like
    weighted: bool
    function: callable
    data_label: str
    function_label: str
    axis_label: str
    title: str
        Default: Title
    fmt: str
        Default: bx (blue, x-Marker)
    
    """

    params, params_cov, function_fit, residuals,reduced_chisquare = least_square_method_fit(xdata,ydata,function,weighted,yerr)
    plt.errorbar(xdata,ydata,yerr=yerr,xerr=xerr, fmt=fmt_data, capsize=10)
    plt.errorbar(xdata, function_fit,yerr=params_cov[1],xerr=params_cov[0], fmt=fmt_fit, label=function_label)

    plt.grid(True)
    plt.legend()
    plt.xlabel(axis_label[0])
    plt.ylabel(axis_label[1])
    plt.title(title)
    return residuals, reduced_chisquare