import numpy as np
from numpy.core import machar
from numpy.core.fromnumeric import sort
from numpy.core.records import array
from numpy.lib.shape_base import column_stack
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt



DataALL = pd.read_csv("NewData.csv")

s =  DataALL
afs = s.iloc[: , 1:]
header = s.head()
z = 10

#for i in range(z):
CS_Mat = np.array([
    s['Calculus'][:] > 99,
    s['DataBase'][:] < 90 ,
    s['LinerAlgebra'][:] > 99 ,
    s['Intro_to_CS'][:] > 99 ,
    s['intro to IS'][:] < 90 ,
    s['Discrete'][:] > 99 ,
    s['Object Oriented'][:] > 99 ,
    s['Statistics'][:] > 99 ,
    s['ProgramingLanguage'][:] > 99 ,
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
    s['LinerAlgebra'][:] < 99 ,
    s['Intro_to_CS'][:] < 99 ,
    s['Intro_to_IS'][:] > 90 ,
    s['Discrete_Math'][:] > 99 ,
    s['ObjectOriented'][:] < 99 ,
    s['Statistics'][:] < 99 ,
    s['ProgramingLanguage'][:] < 99 ,
    s['DifferentialEquation'][:] < 99 ,
    s['Operations_Researsh'][:] > 102 ,
    s['DataStructure'][:] < 99 ,
    s['FileProcessing'][:] > 99 ,
    s['AdvansedMathematics'][:] < 99 ,
    s['Physic'][:] < 99 ,
    s['Stochastic'][:] < 99 ,
    s['Multimedia'][:] > 99 ,
    s['InformationTheory'][:] > 99 ,
    s['SystemAnalysis_And_Design'][:] > 99 ,
])

s2 = sum(CS_Mat.astype(int))

s2 = list(s2)
s3 = sum(IS_Mat.astype(int))

s3 = list(s3)
Is = 0
cs = 0
Department = []
Department_2 = []

###################################
###### [[[Must be N.column be Odd ]]].
###################################
for i in range(len(s2)):
    if(s2[i] == max(s2[i] , s3[i])):
        Department.append(s2[i])
        Department_2.append(1)
    else :
        Department.append(s2[i])
        Department_2.append(0)

DataALL.insert(20 , 'Department_2' ,Department_2)
DataALL.insert(21 , 'Department' ,Department)


DataALL.to_csv(r'\home\abdo\Data\Datadata.csv', index = False)


data  =  pd.read_csv("Datadata.csv")
'''
X  = data.drop(["Departments","Department120"] , axis = 1)
y= data['Department120']

data2 = data["Departments"]


plt.scatter(data2,X['DataBase'])

plt.show()
'''