import numpy as np

def f(x):
    #write the expression here
    f=6*np.exp(-2*x)+2*x**2
    return f

def df(x):
    df=-12*np.exp(-2*x)+4*x
    # df=2*x+2
    return df


count=0

n=0
def bisection_search(l,a,b):
    a=float(a)
    b=float(b)
    print("a,b ={}, {} ".format(a,b))
    global count
    count+=1
    # print(count)
    # print(a,b)
    global n
    if count==1:
        n=np.ceil(np.log(l/(b-a))/np.log(0.5))
    else:
        pass
    if count==n:
        print("Number of iterations= {}".format(count))
        return a,b,(a+b)/2
    else:
        lamda=(b+a)/2
        print("lamda= {}".format(lamda))
        dl=df(lamda)
        print("df(lamda)= {}".format(dl))
        print("----------------------------------------")
        if dl==0:
            print("Number of iterations= {}".format(count))
            return lamda,lamda,lamda
        elif dl>0:
            p,q,o=bisection_search(l,a,lamda)
            return p,q,(p+q)/2
        elif dl<0:
            p,q,o=bisection_search(l,lamda,b)
            return p,q,(p+q)/2

a,b,o=bisection_search(0.0001,-3,5)
print("The optima with Bisection search method= {}".format(o))
