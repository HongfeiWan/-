##使用curve_fit

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
 
#定义函数
def func(x,a,b,c):
    zhishu = a*x+b*(1-x**2)+c
    return zhishu
 
#定义x、y散点坐标
x=[0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.7,3,3.3,3.6]
c=[0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.7,3,3.3,3.6]
x1=[]
for i in range(0,len(x)):
    x1.append(sin(x[i]))
x = np.array(x1)
num = [1.248,0.984,0.971,1.126,1.337,1.466,1.428,1.215,0.917,0.726,0.575,0.503]
num1= []
for i in range(0,len(num)):
    a = num[i]
    b = c[i]
    num1.append(log(a)/log(b))
y = np.array(num1)

#非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)

#获取popt里面是拟合系数
a = popt[0]
b = popt[1]
c = popt[2]

yvals = func(x,a,b,c) #拟合y值

print('系数a:{:.4f}'.format(a))
print('系数b:{:.4f}'.format(b))
print('系数c:{:.4f}'.format(c))
wucha = 0
l1=[]
for i in range(0,6):
    wucha = (func(x[i],a,b,c)-num1[i])**2 + wucha
    l1.append(func(x[i],a,b,c)-num1[i])
print('均方误差：{:.4f}'.format(wucha))
max1=max(l1)
print('最大误差:{:.4f}'.format(max1))

#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('curve_fit')
plt.show()
