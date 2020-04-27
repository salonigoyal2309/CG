#Axonometric projection
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.gca(projection='3d')

faces = [[[100,100,100],[200,100,100],[200,0,100],[100,0,100]],
	[[100,0,100],[100,100,100],[100,100,200],[100,0,200]],
	[[100,100,200],[200,100,200],[200,0,200],[100,0,200]],
	[[200,100,200],[200,100,100],[200,0,100],[200,0,200]],
	[[100,0,100],[100,0,200],[200,0,200],[200,0,100]],
	[[100,100,100],[200,100,100],[200,100,200],[100,100,200]]]

tempFaces = [[[100,100,100],[200,100,100],[200,0,100],[100,0,100]],
	[[100,0,100],[100,100,100],[100,100,200],[100,0,200]],
	[[100,100,200],[200,100,200],[200,0,200],[100,0,200]],
	[[200,100,200],[200,100,100],[200,0,100],[200,0,200]],
	[[100,0,100],[100,0,200],[200,0,200],[200,0,100]],
	[[100,100,100],[200,100,100],[200,100,200],[100,100,200]]]


print(" Axonometric projections ")

print("Enter vector normal :")
n1=int(input())
n2=int(input())
n3=int(input())
a=-n1
b=-n2
c=-n3
print("Enter reference point :")
R0=input().split()
d0=int(R0[0])*n1+int(R0[1])*n2+int(R0[2])*n3
d1=a*n1+b*n2+c*n3

'''
x = np.linspace(-10,600)
y = np.linspace(-10,600)
X,Y = np.meshgrid(x,y)
Z = (d0-X*n1-Y*n2)/n3

ax.plot_surface(X,Y,Z)'''

for i in range(0,len(faces)):
	x=[]
	y=[]
	z=[]
	for j in range(0,4):
		x.append(faces[i][j][0])
		y.append(faces[i][j][1])
		z.append(faces[i][j][2])
		
	ax.plot(x,y,z,c="red")

for i in range(0,len(tempFaces)):
	x=[]
	y=[]
	z=[]
	for j in range(0,4):
		x0=tempFaces[i][j][0]
		y0=tempFaces[i][j][1]
		z0=tempFaces[i][j][2]
		x0=(x0*(d1-a*n1)-y0*a*n2-z0*a*n3+a*d0)/d1
		y0=(y0*(d1-b*n2)-x0*b*n1-z0*b*n3+b*d0)/d1
		z0=(z0*(d1-c*n3)-x0*c*n1-y0*c*n2+c*d0)/d1
		tempFaces[i][j][0]=x0
		tempFaces[i][j][1]=y0
		tempFaces[i][j][2]=z0
		x.append(x0)
		y.append(y0)
		z.append(z0)
	ax.plot(x,y,z,c='blue')

ax.set_xlabel('X')
ax.set_xlim(0,500)
ax.set_ylabel('Y')
ax.set_ylim(0,500)
ax.set_zlabel('Z')
ax.set_zlim(0,500)

plt.show()
