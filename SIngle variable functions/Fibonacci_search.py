import numpy as np


def f(x):
    #enter the expression here
    f=6*np.exp(-2*x)+2*x**2
    return f

# # b=5
# # a=-5
# # l=0.01
# # epslon=0.005
# #f is the list of fibonacci seires expansion.
# limit=(b-a)/l
def fibonacci(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_search(a,b,l,eps,n,k):
    print("a,b ={}, {} ".format(a,b))
    lamda=float(a+(fibonacci(n-2)/fibonacci(n))*(b-a))
    mu=float(a+(fibonacci(n-1)/fibonacci(n))*(b-a))
    print("lamda,mu = {}, {}".format(lamda,mu))
    print("f(lamda), f(mu)= {}, {}".format(f(lamda),f(mu)))
    print("----------------------------------------")
    if f(lamda) > f(mu):
        a=lamda
        lamda=mu
        mu=a+(fibonacci(n-k-1)/fibonacci(n-k))*(b-a)
    else:
        b=mu
        mu=lamda
        lamda=a+(fibonacci(n-k-2)/fibonacci(n-k))*(b-a)

    if k==n-2:
        print("Number of iterations= {}".format(k))
        mu_k=lamda+eps
        if f(lamda)>f(mu):
            # print("fibonacci_search Solution: ",(lamda+b)/2)
            return (lamda+b)/2
        else:
            # print("fibonacci_search Solution: ",(a+mu)/2)
            return (a+mu)/2
    else:
        k += 1
        o=fibonacci_search(a,b,l,eps,n,k)
        return o


o=fibonacci_search(-3,5,0.0001,0.001,27,1)
print("The optima with Fibonacci search method= {}".format(o))
