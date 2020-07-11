import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import chi2
from scipy.stats import chi2_contingency

crD=pd.read_csv('D:\Courses\BSE-BI\BSE\BSE\Statistics-II\Chi-Square\Codes\Dataset\Credit.csv',header="infer")
print(crD.shape)
#Find frequency of a continuous column in discrete bins
for cols in crD.columns:
    print(cols)
freq=crD['Income'].value_counts(bins=4)
print(freq)

#chi square test for independence
ctab=pd.crosstab(crD.Defaultee, pd.cut(crD.Income, [10,54.424,98.494,142.564,186.634], include_lowest=True), margins=False)
print(ctab)
stat, p, dof, expected=chi2_contingency(ctab)
prob=0.95
critical=chi2.ppf(prob,dof)
if(abs(stat)>=critical):
    print('Dependent (Reject H0)')
else:
    print('Independent (Accept H0)')