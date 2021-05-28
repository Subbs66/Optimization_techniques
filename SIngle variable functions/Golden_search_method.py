import numpy as np

def f(x):
    #enter the expression here
    f=6*np.exp(-2*x)+2*x**2
    return f

count=0
def golden_search(l,a,b):
    print("a,b ={}, {} ".format(a,b))
    global count
    count+=1
    # print(type(a),type(b))
    alpha=0.618
    if b-a>=l:
        lamda=a+((1-alpha)*(b-a))
        mu=a+alpha*(b-a)
        print("lamda,mu = {}, {}".format(lamda,mu))
        print("f(lamda), f(mu)= {}, {}".format(f(lamda),f(mu)))
        print("----------------------------------------")
        if f(lamda)>f(mu):
            i,j,o=golden_search(l,lamda,b)
            return i,j,(i+j)/2
        else:
            i,j,o=golden_search(l,a,mu)
            return i,j,(i+j)/2
    else:
        print("Number of iterations= {}".format(count))
        return (a,b,(a+b)/2)


_,_,optima=golden_search(0.0001,-3,5)
print("The optima with Golden search method= {}".format(optima))
