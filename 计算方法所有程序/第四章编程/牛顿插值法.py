#输入数据
n=int(input('n次牛顿插值多项式'))
x0 = float(input('输入您想要算的x'))

#划定房子
x=[]#源数据    
y=[]#源数据
dx=[]
dy=[]
i=0

#创建存储单元
for t in range(0,n):
    dx.append([])
    dy.append([])

#输入源数据
while 1:
    xi = float(input('输入x%d值'%i))
    x.append(xi)
    yi = float(input('输入y%d值'%i))
    y.append(yi)
    i = i+1
    if len (y) == n+1:
        break

def chashang(f1,f2,x1,x2):
    chashang = (f1-f2)/(x1-x2)
    return chashang

#获得表格第一个数据（初始数据的输入）
for i in range(0,n):
    a = chashang(y[i+1],y[i],x[i+1],x[i])
    dy[0].append(a)
    deltax=x[i+1]-x[i]
    dx[0].append(deltax)
    print(a)
    #if i > 1:

#迭代        
for i in range(0,n):#0,1,2
    for j in range(0,n-i-1):#0,1
        if n-i-1 == 0:
            break
        else:
            
            #deltax2=dx[i][j+1]+dx[i][j]
            deltax2 = x[j+2+i]-x[j]
            b = (dy[i][j+1]-dy[i][j])/deltax2
            dy[i+1].append(b)
            
            dx[i+1].append(deltax2)
xishu = 1
N = y[0]
for i in range(0,n):
    print(N)
    xishu = (x0 - x[i])*xishu
    N = N+dy[i][0]*xishu
    


