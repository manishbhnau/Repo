import numpy as np
import pandas as pd
import scipy as sp
from scipy import linalg
from scipy.linalg import null_space
from scipy.stats import chi2
from scipy.stats import chi2_contingency
#import keras as kr
#from  keras.layers import Input, Dense
#from keras.models import Model
#dataset=np.loadtxt('E:\Research\Models-Practice\Keras-codes\pima-indians-diabetes.data.txt', delimiter=',')
#nlen= len(dataset)
#ntrain=int(nlen/3)
#print(nlen, ntrain)
#X=dataset[:,0:8]
#Y=dataset[:,8]
#input=Input(shape=(8,))
#hidden=Dense(3, activation='relu')(input)
#output=Dense(1, activation='sigmoid')(hidden)
#model=Model(inputs=input, outputs=output)
#print(model.summary())
crD=pd.read_csv('D:\Courses\BSE-BI\BSE\BSE\Statistics-II\Chi-Square\Codes\Dataset\Credit.csv',header="infer")
print(crD.shape)
for cols in crD.columns:
    print(cols)
freq=crD['Income'].value_counts(bins=4)
print(freq)
ctab=pd.crosstab(crD.Defaultee, pd.cut(crD.Income, [10,54.424,98.494,142.564,186.634], include_lowest=True), margins=False)
print(ctab)
stat, p, dof, expected=chi2_contingency(ctab)
prob=0.95
critical=chi2.ppf(prob,dof)
if(abs(stat)>=critical):
    print('Dependent (Reject H0)')
else:
    print('Independent (Accept H0)')