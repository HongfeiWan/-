import matplotlib.pyplot as plt
import numpy as np


x=[100,121,144,169]
y=[10,11,12,13]
calculate_x = x
plt.plot(x,y,'.')
plt.show()

#多项式拟合函数
def ax_bfit(x,y,calculate_x,n):
    x=np.array(x)
    y=np.array(y)
    calculate_x = np.array(calculate_x)
    fit_coef = np.ployfit(x,y,n)
    calculate_y=np.polyval(fit_coef,calculate_x)

    fit_coef=[round(i,3) for i in fit_coef]
    plt.plot(x,y,'^')
    plt.plot(calculate_x,calculate_y)
    plt.show()
    return fit_coef,calculate_y

ax_bfit(x,y,calculate_x,2)
