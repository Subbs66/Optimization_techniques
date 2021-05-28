import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def f2(v1,v2):
    #write the expression here
    f=(3 - v1)**2 + 7*(v2 - v1**2)**2
    # f=(v1-v2**3)**2+3*(v1-v2)**4
    # f=(v1-2)**4+(v1-2*v2)**2
    return f

def rang(x,y,j):
    if j==0:
        l=x-2
        u=x+2
        return l,u,y
    elif j==1:
        l=y-2
        u=y+2
        return l,u,x

def golden_search(l,a,b,c,j):
    # print(a,b)
    # print(type(a),type(b))
    alpha=0.618
    if j==0:
        if abs(b-a)>=0.0001:
            lamda=a+((1-alpha)*(b-a))
            mu=a+alpha*(b-a)
            if f2(lamda,c)>f2(mu,c):
                i,j,o,c=golden_search(l,lamda,b,c,j)
                return i,j,(i+j)/2,c
            else:
                i,j,o,c=golden_search(l,a,mu,c,j)
                return i,j,(i+j)/2,c
        else:
            return (a,b,(a+b)/2,c)
    elif j==1:
        if abs(b-a)>=0.0001:
            lamda=a+((1-alpha)*(b-a))
            mu=a+alpha*(b-a)
            if f2(c,lamda)>f2(c,mu):
                i,j,c,o=golden_search(l,lamda,b,c,j)
                return i,j,c,(i+j)/2
            else:
                i,j,c,o=golden_search(l,a,mu,c,j)
                return i,j,c,(i+j)/2
        else:
            return (a,b,c,(a+b)/2)

def Golden_search_cross(l,lx,ly,ux,uy):
    alpha=0.618
    if ((((lx-ux)**2)+((ly-uy)**2) )**0.5)>=l:
        lamdax=lx+((1-alpha)*(ux-lx))
        lamday=ly+((1-alpha)*(uy-ly))
        mux=lx+alpha*(ux-lx)
        muy=ly+alpha*(uy-ly)
        if f2(lamdax,lamday)>f2(mux,muy):
            nx,ny=Golden_search_cross(l,lamdax,lamday,ux,uy)
            return nx,ny
        else :
            nx,ny=Golden_search_cross(l,lx,ly,mux,muy)
            return nx,ny
    else:
        return (ux+lx)/2,(uy+ly)/2


def hooke_and_jeeves(l,x,y):
    global count
    count+=1
    ox,oy=x,y
    nx,ny=x,y
    if count==1:
        global lox,loy
        lox,loy=x,y
    lamda=[]
    print("f(xk)= {}".format(f2(lox,loy)))
    # if count%50==0:
    #     print("Intial point= ({},{})".format(x,y))
    print("Intial point= ({},{})".format(x,y))
    for j in range(2):
        k,n,m=rang(nx,ny,j)
        nox,noy=nx,ny
        _,_,nx,ny=golden_search(l,k,n,m,j)
        # if count%50==0:
        #     print("lamda= {},{}".format(nx-nox,ny-noy))
        #     print("point after updating= ({},{})".format(nx,ny))
        if j==0:
            print("lamda{}= {}".format(j+1,nx-nox))
        else:
            print("lamda{}= {}".format(j+1,ny-noy))
        print("point after updating= ({},{})".format(nx,ny))
    dist=((((nx-lox)**2)+((ny-loy)**2) )**0.5)
    if dist<l:
        print("----------------------------------------")
        print("Number of iterations= {}".format(count))
        return nx,ny
    else:
        d1,d2=nx-lox,ny-loy
        lox,loy=nx,ny
        lx=nx-2*(1/np.sqrt(1+(d2/d1)**2))
        ux=nx+2*(1/np.sqrt(1+(d2/d1)**2))
        cap=2*(1/np.sqrt(1+(d2/d1)**2))/d1
        ly=ny-d2*cap
        uy=ny+d2*cap
        nox,noy=nx,ny
        nx,ny=Golden_search_cross(l,lx,ly,ux,uy)
        cap=(nx-nox)/d1
        print("d= ({},{})".format(d1,d2))
        print("lamda cap= {}".format(cap))
        # print((nx-nox)/d1,(ny-noy)/d2)
        print("point after updating= ({},{})".format(nx,ny))
        print("----------------------------------------")
        p,q=hooke_and_jeeves(l,nx,ny)
        return p,q



count=0
lox,loy=0,0
x,y=hooke_and_jeeves(0.0001,0,0)
print("The optima with hook and jeeve's method= ({},{})".format(x,y))


