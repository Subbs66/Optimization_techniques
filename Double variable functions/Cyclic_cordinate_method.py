import numpy as np

def f2(v1,v2):
    #write the expression here
    f=(3 - v1)**2 + 7*(v2 - v1**2)**2
    # f=v2*(v2+2)+v1
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
count=0
def cyclic_cordinate(l,x,y):
    global count
    count+=1
    ox,oy=x,y
    nx,ny=x,y
    if count%50==0:
        print("Intial point= ({},{})".format(x,y))
    for j in range(2):
        k,n,m=rang(nx,ny,j)
        nox,noy=nx,ny
        _,_,nx,ny=golden_search(l,k,n,m,j)
        if count%50==0:
            print("lamda= {},{}".format(nx-nox,ny-noy))
            print("point after updating= ({},{})".format(nx,ny))
    if count%50==0:
        print("----------------------------------------")
    dist=((((nx-ox)**2)+((ny-oy)**2) )**0.5)
    if dist<l:
        print("Number of iterations= {}".format(count))
        return nx,ny
    else:
        p,q=cyclic_cordinate(l,nx,ny)
        return p,q

x,y=cyclic_cordinate(0.0003,0,0)
print("The optima with Newton's method= ({},{})".format(x,y))

# _,_,x,y=golden_search(0.01,-3,5,0,1)
# print(x,y)
