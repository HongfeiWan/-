import numpy as np  
import matplotlib.pyplot as plt 
  
# 随机点输入
X = [0.4,0.5,0.6,0.7] 
Y = [0.56,0.29,0,-0.30]
plt.plot(X, Y, 'ro')  
plt.show()

####根据方程组的系数矩阵和方程右端构成的向量来求解未知量
def linear_regression(x, y):
    N = len(x) 
    sumx = sum(x) 
    sumy = sum(y)
    sumx2=0
    sumxy=0
    for i in range (0,N):
        sumx2 = sumx2 + X[i]**2
        sumxy = sumxy + X[i]*Y[i]
    A = np.mat([[N, sumx], [sumx, sumx2]]) 
    b = np.array([sumy, sumxy]) 
    return np.linalg.solve(A, b)
a0, a1 = linear_regression(X, Y)

####

# 生成拟合直线的绘制点
N = len(X) - 1
R = X[N]
_X = [0, R]  
_Y = [a0 + a1 * x for x in _X] 
plt.plot(X, Y, 'ro', _X, _Y, 'b', linewidth=2)  
plt.title("y = {} + {}x".format(a0, a1))  
plt.show()
####


