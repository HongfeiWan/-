##使用curve_fit

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 
#自定义函数 e指数形式
def func(x, a, b,c):
    zhishu = a*(x-100)**3+b*(x-100)**2+c
    return zhishu
 
#定义x、y散点坐标
x=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
x = np.array(x)
num = [0.5,1.8,2.6,3.1,3.5,3.8,3.95,4.1,4.2,4.2,4.2,4.2,4.2,4.2,4.25,4.3,4.5,5.2,6.2,7.2]
y = np.array(num)
 
#非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
#获取popt里面是拟合系数

a = popt[0] 
b = popt[1]
c = popt[2]
yvals = func(x,a,b,c) #拟合y值


print('系数a:{:.6f}'.format(a))
print('系数b:{:.4f}'.format(b))
print('系数c:{:.4f}'.format(c))
wucha = 0
l1=[]
for i in range(0,6):
    wucha = (func(x[i],a,b,c)-num[i])**2 + wucha
    l1.append(func(x[i],a,b,c)-num[i])
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
