if __name__ =="__main__":
    typeb_length1 = 0.020412414523193152
    uncperiod = [0.01836081, 0.01836112, 0.01832736]
    from fit import linear_fit,fit_ls
    tenperiods = [14.25,13.75,13.63,16.59,16.47,16.44]
    period1 = tenperiods/10
    length1 = [54.6,54.6,54.6,80.9,80.9,80.9]
    fit_ls(**2, length1,linear_fit)