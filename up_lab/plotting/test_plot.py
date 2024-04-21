if __name__ =="__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.scale as matplotlibscale

    #help(matplotlibscale.ScaleBase)
    #Example data
    xdata = [123,345,340,346,645,234,356]
    ydata = [2,4,5,9,3,6,3]
    def linfunc(x,a,b):
        return a*x+b
    #Test array_plot
    #array_plot(xdata, ydata,yerr=0.4,weighted=True)

    plt.errorbar(xdata,ydata, yerr=0.3,)
    plt.show()

    #Test array_plot
    array_plot(xdata, ydata,yerr=0.4,weighted=True)

    def tuple_return_test(a,b,c):
        returnval = [a,b,c]
        return *returnval,
    one = np.array([1])
    a,b,c = tuple_return_test(one,True,'Love')
    print(a,b)
    print(type())
    from plot import array_plot
    tenperiods = [14.25,13.75,13.63,16.59,16.47,16.44]
    length = [54.6,54.6,54.6,80.9,80.9,80.9]
    periodplot = (tenperiods/10)**2



    
    print(array_plot(periodplot, length, ))