# coding: utf-8
import numpy
import matplotlib.pyplot as plt
import time,sys
nx=41
dx=2/(nx-1)
nt=25
dt=0.025
c=1
u=numpy.ones(nx) #defining an array with nx elements long with every value equal to one
u[int(.5/dx):int(1/dx+1)]=2
print(u)
plt.plot(numpy.linspace(0,2,nx),u)
plt.show()
