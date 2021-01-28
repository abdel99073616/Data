import numpy as np
from numpy.core import machar
from numpy.core.fromnumeric import sort
from numpy.core.records import array
from numpy.lib.shape_base import column_stack
import pandas as pd
import matplotlib

DataALL = pd.read_csv("datalast.csv")

s =  DataALL
afs = s.iloc[: , 1:]
header = s.head()
z = 5
#for i in range(z):
CS_Mat = np.array([
    s['Calculus'][:] > 99,
    s['DataBase'][:] < 90 ,
    s['Liner Algebra'][:] > 99 ,
    s['intro to computer sceince'][:] > 99 ,
    s['intro to IS'][:] < 90 ,
    s['Discrete'][:] > 99 ,
    s['Object Oriented'][:] > 99 ,
    s['Statistics'][:] > 99 ,
    s['Computer Programing'][:] > 99 ,
    s['Defferental Equation'][:] > 99 ,
    s['Operations Researsh'][:] > 102 ,
    s['Data Strucure'][:] < 99 ,
    s['File Processing'][:] < 99 ,
    s['Advansed Mathematics'][:] > 99 ,
    s['Physic'][:] > 99 ,
    s['Stotastic'][:] > 99 ,
    s['Multimedia'][:] < 99 ,
    s['information theory'][:] < 99 ,
    s['system analysis and design'][:] < 99 ,
    ])
IS_Mat = np.array([
    s['Calculus'][:] < 99,
    s['DataBase'][:] > 90 ,
    s['Liner Algebra'][:] < 99 ,
    s['intro to computer sceince'][:] < 99 ,
    s['intro to IS'][:] > 90 ,
    s['Discrete'][:] > 99 ,
    s['Object Oriented'][:] < 99 ,
    s['Statistics'][:] < 99 ,
    s['Computer Programing'][:] < 99 ,
    s['Defferental Equation'][:] < 99 ,
    s['Operations Researsh'][:] > 102 ,
    s['Data Strucure'][:] < 99 ,
    s['File Processing'][:] > 99 ,
    s['Advansed Mathematics'][:] < 99 ,
    s['Physic'][:] < 99 ,
    s['Stotastic'][:] < 99 ,
    s['Multimedia'][:] > 99 ,
    s['information theory'][:] > 99 ,
    s['system analysis and design'][:] > 99 ,
])

s2 = sum(CS_Mat.astype(int))

s2 = list(s2)
s3 = sum(IS_Mat.astype(int))

s3 = list(s3)
Is = 0
cs = 0
Department = []
###################################
###### [[[Must be N.column be Odd ]]].
###################################
for i in range(len(s2)):
    if(s2[i] == max(s2[i] , s3[i])):
        Department.append(s2[i])
    else :
        Department.append(s2[i])
DataALL.insert(20 , 'Department120' ,Department)


DataALL.to_csv(r'D:\Graduation\Graduation-Project/data_dep120.csv', index = False)

