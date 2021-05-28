import numpy as np

def f2(v1,v2):
    #write the expression here
    f=(3 - v1)**2 + 7*(v2 - v1**2)**2
    return f

def rang(x,y,j):
    if j==0:
        l=x-10
        u=x+10
        return l,u,y
    elif j==1:
        l=y-10
        u=y+10
        return l,u,x

def golden_search(l,a,b,c,j):
    alpha=0.618
    if j==0:
        if abs(b-a)>=l:
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


def mod(d):
    for i in range(len(d)):
        m=np.sum([j**2 for j in d])
        m=np.sqrt(m)
    return m

def dvector(lambda_lst,d_i):
    a_j,b_j = [[0,0],[0,0]],[[0,0],[0,0]]
    for i in range(0,2):
        if lambda_lst[i] == 0:
            a_j[i] =  d_i[0]
        else:
            for k in range(i,2):
                a_j[i] += np.multiply(lambda_lst[k],d_i[k])

        if i == 0:
            b_j[i] = a_j[i]
        else:
            for k in range(0,i):
                a_j[i] -= np.multiply(np.dot(a_j[i],d_i[k]),d_i[k])
            b_j[i] = a_j[i]
        d_i[i] =b_j[i]/np.linalg.norm(b_j[i])
    return d_i

count=0
def rosenbrocks(l,x,y,d):
    # print(d)
    global count
    global lamda
    count+=1
    ox,oy=x,y
    nx,ny=x,y
    print("Intial point= ({},{})".format(x,y))
    if count==1:
        nox,noy=nx,ny
        for j in range(2):
            k,n,m=rang(nx,ny,j)
            nox,noy=nx,ny
            _,_,nx,ny=golden_search(l,k,n,m,j)
            lamb=[nx-nox,ny-noy]
            lamda[j]=lamb[j]
            print("lamda= {}".format(lamda[j]))
            print("point after updating= ({},{})".format(nx,ny))
    else:

        for j in range(2):
            nox,noy=nx,ny

            p=d[j]
            d1,d2=p[0],p[1]
            lx=nx-2*(1/np.sqrt(1+(d2/d1)**2))
            ux=nx+2*(1/np.sqrt(1+(d2/d1)**2))
            cap=2*(1/np.sqrt(1+(d2/d1)**2))/d1
            ly=ny-d2*cap
            uy=ny+d2*cap
            nx,ny=Golden_search_cross(l,lx,ly,ux,uy)
            try:
                lamda[j]=(nx-nox)/d1
                if type(lamda[j])!='int':
                    lamda[j]=(ny-noy)/d2
            except:
                lamda[j]=(ny-noy)/d2

            print("point after updating= ({},{})".format(nx,ny))

    print("lamda= {}".format(lamda))
    dist=((((nx-ox)**2)+((ny-oy)**2) )**0.5)
    if dist<l:
        print("----------------------------------------")
        print("Number of iterations= {}".format(count))
        return nx,ny
    else:
        nd=dvector(lamda,d)
        print("new d vector is {}".format(nd))
        print("----------------------------------------")
        p,q=rosenbrocks(l,nx,ny,nd)
        return p,q

d=np.random.rand(2,2)
for j in range(2):
    for i in range(2):
        if i==j:
            d[i,j]=1
        else:
            d[i,j]=0
lamda=[0 for j in range(len(d))]
x,y=rosenbrocks(0.0003,0,0,d)
print("The optima with Rosenbrock's method= ({},{})".format(x,y))
