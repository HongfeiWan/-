from math import *
from sympy import *
n = 1
k = 1
p = 1
output = 0
def f(t):
    hanshu = e**(t/3)+(t/7)**6-1
    return hanshu
lx = []
ly = []
cishu = int(input('你想用几次插值公式？'))
cishu = cishu + 1
x0 = float(input('输入你想要算的点'))
while 1:
    x = float(input('请输入第%d个点的横坐标'%n))
    y = float(f(x))
    n = n+1
    lx.append(x)
    ly.append(y)
    if n == cishu+1:
        break
print('点的集合为：\n','x=',lx,'\n','y=',ly)
for j in range(0,len(ly)):
    for k in range(0,len(lx)):
        if j != k:
            fenzi = (x0-lx[k])
            fenmu = (lx[j]-lx[k])
            p = (fenzi/fenmu)*p
        if j == k:
            continue
    z = p * ly[j]
    output = output + z
    p = 1
cishu = cishu-1
print('%d次拉格朗日插值多项式的结果为：'%cishu,output)
del(x)



#求导########################################
x = symbols("x")                            #
a = diff(e**(x/3)+(x/7)**6-1,x)             #
for i in range(cishu):                      #
    b = diff(a,x)                           #
    a = b                                   #
daoshulist=[]                               #
for i in lx:                                #
    daoshu = a.evalf(subs={'x':i})          #
    daoshulist.append(daoshu)               #
fenzi=max(daoshulist)                       #
#############################################



del(n)
n=cishu+1
for i in range(1,cishu+1):
    n = i * n
############################################################################
w=1
for xi in lx:
    w = w*(x0-xi)
wucha = abs(fenzi*w/n)

print('截断误差为{:.4f}'.format(wucha))


        













    
    
