from plot import array_plot

#Example data
xdata = [123,345,340,346,645,234,356]
ydata = [2,4,5,9,3,6,3]
def linfunc(x,a,b):
    return a*x+b
#Test array_plot
array_plot(xdata, ydata,yerr=0.4,weighted=True)