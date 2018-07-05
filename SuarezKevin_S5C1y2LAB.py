import matplotlib.pylab as plt
from scipy import fftpack
import matplotlib.cm as cm

imagen = plt.imread('moonlanding.png')
transfor = fftpack.fft2(imagen) 
tShift = fftpack.fftshift(transfor) 
a=len(tShift[:,0])
b=len(tShift[0])

print a
print tShift

print tShift[0,0]

plt.figure()
plt.imshow(abs(tShift),vmax=300)
plt.show()
for i in range(a):
	for j in range(b):
		if(tShift[i,j]>=200):
			tShift[i,j]=0	
			print i,j, tShift[i,j]

plt.figure()
plt.imshow(abs(tShift),vmax=300)
plt.show()
inversa=fftpack.ifft2(tShift)
#print inversa
git add SuarezKevin_S5C1y2LAB.py
#plt.figure()
#plt.imshow(abs(inversa),vmax=300)
#plt.show()

