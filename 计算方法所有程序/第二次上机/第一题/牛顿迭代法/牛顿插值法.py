#输入数据
from math import *
from sympy import *
n=int(input('n次牛顿插值多项式'))
x0 = float(input('输入您想要算的x'))

#划定房子
xa=[]#源数据    
ya=[]#源数据
dx=[]
dy=[]
i=0

def f(t):
    hanshu = e**(t/3)+(t/7)**6-1
    return hanshu

#创建存储单元
for t in range(0,n):
    dx.append([])
    dy.append([])

#输入源数据
while 1:
    xi = float(input('输入x%d值'%i))
    xa.append(xi)
    yi = float(f(xi))
    ya.append(yi)
    i = i+1
    if len (ya) == n+1:
        break

def chashang(f1,f2,x1,x2):
    chashang = (f1-f2)/(x1-x2)
    return chashang

#获得表格第一个数据（初始数据的输入）
for i in range(0,n):
    a = chashang(ya[i+1],ya[i],xa[i+1],xa[i])
    dy[0].append(a)
    deltax=xa[i+1]-xa[i]
    dx[0].append(deltax)
    
    #if i > 1:

#迭代        
for i in range(0,n):#0,1,2
    for j in range(0,n-i-1):#0,1
        if n-i-1 == 0:
            break
        else:
            
            #deltax2=dx[i][j+1]+dx[i][j]
            deltax2 = xa[j+2+i]-xa[j]
            b = (dy[i][j+1]-dy[i][j])/deltax2
            dy[i+1].append(b)
            
            dx[i+1].append(deltax2)
xishu = 1
N = ya[0]
for i in range(0,n):
    
    xishu = (x0 - xa[i])*xishu
    N = N+dy[i][0]*xishu
print('%d次拉格朗日插值多项式的结果为'%n,N)

cishu = n

#求导
x = symbols("x")
a = diff(e**(x/3)+(x/7)**6-1,x)
for i in range(cishu):
    b = diff(a,x)
    a = b
daoshulist=[]
for i in xa:
    daoshu = a.evalf(subs={'x':i})
    daoshulist.append(daoshu)
fenzi=max(daoshulist)
###########################
del(n)
n=cishu+1
for i in range(1,cishu+1):
    n = i * n
###########################
w=1
for xi in xa:
    w = w*(x0-xi)
wucha = abs(fenzi*w/n)

print('截断误差为{:.4f}'.format(wucha))


