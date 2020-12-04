import matplotlib.pyplot as plt 
import numpy as np 
x=[0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.7,3,3.3,3.6]
y=[1.248,0.984,0.971,1.126,1.337,1.466,1.428,1.215,0.917,0.726,0.575,0.503]
a=np.polyfit(x,y,6)#用6次多项式拟合x，y数组
b=np.poly1d(a)#拟合完之后用这个函数来生成多项式对象
c=b(x)#生成多项式对象之后，就是获取x在这个多项式处的值
plt.scatter(x,y,marker='o',label='original datas')#对原始数据画散点图
plt.plot(x,c,ls='--',c='red',label='fitting with second-degree polynomial')#对拟合之后的数据，也就是x，c数组画图
plt.legend()
plt.show()
print('拟合多项式为({})+({})x+({})x^2+({})x^3+({})x^4+({})x^5+({})x^6'.format(b[0],b[1],b[2],b[3],b[4],b[5],b[6]))
wucha = 0
l1=[]
for i in range(0,6):
    wucha = (b(x[i])-y[i])**2 + wucha
    l1.append(b(x[i])-y[i])
print('均方误差：{:.4f}'.format(wucha))
max1=max(l1)
print('最大误差:{:.4f}'.format(max1))
