import numpy as np  
import matplotlib.pyplot as plt 
  

# 随机点输入
X = [19,25,31,38,44] 
Y = [19.0,32.3,49.0,73.3,97.8]
plt.plot(X, Y, 'ro')  
plt.show()
####

# 生成系数矩阵A 
def gen_coefficient_matrix(X, Y):  
    N = len(X) 
    m = 3
    A = []
    
    for i in range(m):
        a = []
        b=0
        for j in range(m):
            b= b + X[i] ** (i+j)
            a.append(b)
            A.append(a)
    return A 
  
# 计算方程组的右端向量b 
def gen_right_vector(X, Y):  
    N = len(X) 
    m = 3
    b = []
    c = 0
    for i in range(m):
        c = c + X[i]**i*Y[i]
        b.append(c) 
    return b 
  
A = gen_coefficient_matrix(X, Y)  
b = gen_right_vector(X, Y) 
  
a0, a1, a2 = np.linalg.solve(A, b)

####

# 生成拟合曲线的绘制点
N = len(X) - 1
R = X[N]
_X = [0, R] 
_Y = [a0 + a1*x + a2*x**2 for x in _X]
plt.plot(X, Y, 'ro', _X, _Y, 'b', linewidth=2)  
plt.title("y = {} + {}x + {}$x^2$ ".format(a0, a1, a2))  
plt.show()

