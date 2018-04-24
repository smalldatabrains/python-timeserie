import numpy as np
import matplotlib.pyplot as plt

def autocorrelate(x):
	norm=np.sum(x**2)
	c=np.correlate(x,x,mode='full')/norm
	plt.plot(c)
	plt.title('autocorrelation')
	plt.show()
	return c

