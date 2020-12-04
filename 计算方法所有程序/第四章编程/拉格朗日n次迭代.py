n = 1
k = 1
p = 1
output = 0
lx = []
ly = []
cishu = int(input('你想用几次插值公式？'))
x0 = float(input('输入你想要算的点'))
while 1:
    x = float(input('请输入第%d个点的横坐标'%n))
    y = float(input('请输入第%d个点的纵坐标'%n))
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
print('%d次拉格朗日插值多项式的结果为：'%cishu,output)

        













    
    
