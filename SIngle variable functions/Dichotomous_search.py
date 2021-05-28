import numpy as np

def f(x):
    #enter the expression here
    f=6*np.exp(-2*x)+2*x**2
    return f

count=0
def dichotomous_search(l,epslon,a,b):
    print("a,b ={}, {} ".format(a,b))
    global count
    count+=1
    # print(type(a),type(b))
    alpha=0.5
    if b-a>=l:
        lamda=a+((1-alpha)*(b-a))-epslon
        mu=a+alpha*(b-a)+epslon
        print("lamda,mu = {}, {}".format(lamda,mu))
        print("f(lamda), f(mu)= {}, {}".format(f(lamda),f(mu)))
        print("----------------------------------------")
        if f(lamda)>f(mu):
            i,j,o=dichotomous_search(l,epslon,lamda,b)
            return i,j,(i+j)/2
        else:
            i,j,o=dichotomous_search(l,epslon,a,mu)
            return i,j,(i+j)/2
    else:
        print("Number of iterations= {}".format(count))
        return (a,b,(a+b)/2)

_,_,optima=dichotomous_search(0.002,0.0002,-3,5)
print("The optima with Dichotomous search method= {}".format(optima))
