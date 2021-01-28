from numpy import random
from pandas import DataFrame

x = random.uniform(size=(2, 3))

s = random.uniform(60,120,size=(3000,19))

data = [list( map(int,i) ) for i in s]

df = DataFrame (data,columns=['Calculus','DataBase','LinerAlgebra','Intro_to_CS','Intro_to_IS',
                  'Discrete_Math','ObjectOriented','Statistics','ProgramingLanguage',
                  'DifferentialEquation','Operations_Researsh','DataStructure','FileProcessing','AdvancedMathematics',
                  'Physics','Stochastic','Multimedia','InformationTheory','SystemAnalysis_And_Design'])

df.to_csv(r'/home/abdo/Data/NewData.csv', index = False)
