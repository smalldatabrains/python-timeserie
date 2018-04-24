#Fourier transform of a 1d signal
import numpy as np
import math
import matplotlib.pyplot as plt

x=np.arange(0,100)
u=np.sin(x)*x
plt.plot(x,u)
plt.show()

#let u be our signal

N=len(u)
k=np.arange(0,N)
Fn=[]
freq=[]

#Fourier basis
for n in range(0,N):
	f=np.exp(1j*2*math.pi*n/N*k)
	Fn.append(f)
	freq.append(n/N)

print(len(Fn))
print(len(freq))

#check orthogonality of the fourier basis
for f in range(len(Fn)):
	print("f equals",f)
	other=[x for i,x in enumerate(Fn) if i!=f]
	for l in range(len(other)):
		dot=np.dot(Fn[f],other[l])
		if dot<0.000001: #checking if the scalar is small
			print(l)
			print("True")

TF=[]
#decomposition in Fourier basis
for f in range(len(Fn)):
	tfu=np.dot(u,Fn[f].conjugate())
	print(tfu)
	TF.append(tfu/N)

#ploting of the spectrum
module=map(abs,TF)
plt.plot(freq,TF)
plt.show()