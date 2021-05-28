import numpy as np

def f(x):
    #write the expression here
    f=6*np.exp(-2*x)+2*x**2
    return f

def df(x):
    df=-12*np.exp(-2*x)+4*x
    # df=2*x+2
    return df

def ddf(x):
    ddf=24*np.exp(-2*x)+4
    return ddf

def newton_method(l,p):
    lamda=p
    count=0
    while True:
        count+=1
        print("lamda= {}".format(lamda))
        olamda=lamda
        dl=df(lamda)
        ddl=ddf(lamda)
        print("df(lamda), ddf(lamda)= {}, {}".format(dl,ddl))
        lamda=lamda-(dl/ddl)
        print("Updated lamda= {}".format(lamda))
        print("----------------------------------------")
        dist = np.linalg.norm(olamda-lamda)
        if dist<l:
            print("Number of iterations= {}".format(count))
            return lamda
        if abs(dl)<l:
            print("Number of iterations= {}".format(count))
            return lamda

o=newton_method(0.0001,5)
print("The optima with Newton's method= {}".format(o))
