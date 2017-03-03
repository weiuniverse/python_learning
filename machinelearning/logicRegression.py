import numpy as np


scores=[3.0,1.2,0.2]
Prob=[0,0,0]
for i in range(3):
    Prob[i]=np.exp(scores[i])
P=sum(Prob)
print(P)
Prob=Prob/P
print(Prob)


