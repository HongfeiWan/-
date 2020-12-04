import xlrd
data = xlrd.open_workbook('1.xlsx')
table = data.sheet_by_name('Sheet1')
hang = table.nrows
lie = table.ncols

def NIC(A):
    y = (-1/11)*A+(30/11)
    y = ('{:.2f}'.format(y))
    return y
def SJB1(B):
    y = (-1/390)*B+(730/390)
    y = ('{:.2f}'.format(y))
    return y
def fz(N):
    y = (-1/655)*N+(1130/655)
    y = ('{:.2f}'.format(y))
    return y
def my(Nm):
    y = (-1/28)*Nm+(40/28)
    y = ('{:.2f}'.format(y))
    return y
############################################
def SJB11(B):
    y = (-1/390)*B+(730/390)
    y = ('{:.2f}'.format(y))
    return y
def fz1(N):
    y = (-1/1223)*N+(1480/1223)
    y = ('{:.2f}'.format(y))
    return y
def my1(Nm):
    y = (-1/28)*Nm+(40/28)
    y = ('{:.2f}'.format(y))
    return y
########################################################3
NIClist=[]#1
SJB1list=[]
fzilist=[]
myilist=[]
second=[]#2
SJB1list1=[]
fzilist1=[]
myilist1=[]
third=[]#3
for i in range(0,hang):
    cel_B = table.cell(i,1).value
    NICi = NIC(cel_B)
    NIClist.append(eval(NICi))
    
    cel_C = table.cell(i,2).value
    SJBi = SJB1(cel_C)
    if eval(SJBi)>= 1:
        SJB1list.append(1)
    elif eval(SJBi) <= 0:
        SJB1list.append(0)
    else:
        SJB1list.append(eval(SJBi))

    cel_D = table.cell(i,3).value
    fzi = fz(cel_D)
    if eval(fzi)>= 1:
        fzilist.append(1)
    elif eval(SJBi) <= 0:
        fzilist.append(0)
    else:
        fzilist.append(eval(fzi))

    cel_E = table.cell(i,4).value
    myi = my(cel_E)
    if eval(myi)>= 1:
        myilist.append(1)
    elif eval(myi) <= 0:
        myilist.append(0)
    else:
        myilist.append(eval(myi))
#########################################################
    cel_F = table.cell(i,5).value
    SJBi1 = SJB11(cel_F)
    if eval(SJBi1)>= 1:
        SJB1list1.append(1)
    elif eval(SJBi1) <= 0:
        SJB1list1.append(0)
    else:
        SJB1list1.append(eval(SJBi1))

    cel_G = table.cell(i,6).value
    fzi1 = fz1(cel_G)
    if eval(fzi1)>= 1:
        fzilist1.append(1)
    elif eval(fzi1) <= 0:
        fzilist1.append(0)
    else:
        fzilist1.append(eval(fzi1))

    cel_H = table.cell(i,7).value
    myi1 = my(cel_H)
    if eval(myi1)>= 1:
        myilist1.append(1)
    elif eval(myi1) <= 0:
        myilist1.append(0)
    else:
        myilist1.append(eval(myi1))
#################################################################

for i in range(0,hang):
    secondi=min(SJB1list[i],fzilist[i],myilist[i])
    second.append(secondi)
    thirdi=min(SJB1list1[i],fzilist1[i],myilist1[i])
    third.append(thirdi)
    
#########################################
zhangjiao = []
for i in range(0,hang):
    cel_I = table.cell(i,8).value
    if cel_I == '':
        zhangjiao.append(0)
    else:
        
        if cel_I >= 19:
            zhangjiao.append(-2)
        elif cel_I < 19 :
            zhangjiao.append(0)
#############################################
ganshe = []
for i in range(0,hang):
    cel_J = table.cell(i,9).value
    if cel_J == 'Y':
        ganshe.append(-2)
    else:
        ganshe.append(0)
###############################################
weiyi = []
for i in range(0,hang):
    cel_K = table.cell(i,10).value
    if cel_K == '':
        weiyi.append(0)
    else:
        
        if cel_K >= 20:
            weiyi.append(-4)
        elif cel_K < 20 :
            weiyi.append(0)
##################################################

sumend=[]
for i in range(0,hang):
    sum1=NIClist[i]+second[i]+third[i]+zhangjiao[i]+ganshe[i]+weiyi[i]
    if sum1 <0:
        sum1 = 0
    sum1 = ('{:.2f}'.format(sum1))
    sumend.append(sum1)










































    
    
