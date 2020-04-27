#cabinet projection
from graphics import *
from math import *
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


print("Cabinet projections ")


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
	
matxy=[[1,0,0],[0,1,0],[0.5*cos(radians(63.4)),0.5*sin(radians(63.4)),0]]
matyz=[[0,1,0],[0,0,1],[0,0.5*cos(radians(63.4)),0.5*sin(radians(63.4))]]
matxz=[[0,0,1],[1,0,0],[0.5*cos(radians(63.4)),0,0.5*sin(radians(63.4))]]
choice=int(input("Enter the plane:\n XY plane=1\nYZ plane=2\nXZ plane=3:"))
if(choice==1):
	for i in range(0,len(tempFaces)):
		x=[]
		y=[]
		z=[]
		for j in range(0,4):
			tempFaces[i][j][0]=tempFaces[i][j][0]*matxy[0][0]+tempFaces[i][j][1]*matxy[1][0]+tempFaces[i][j][2]*matxy[2][0]
			tempFaces[i][j][1]=tempFaces[i][j][1]*matxy[0][1]+tempFaces[i][j][1]*matxy[1][1]+tempFaces[i][j][2]*matxy[2][1]
			tempFaces[i][j][2]=tempFaces[i][j][0]*matxy[0][2]+tempFaces[i][j][1]*matxy[1][2]+tempFaces[i][j][2]*matxy[2][2]
			x.append(tempFaces[i][j][0])
			y.append(tempFaces[i][j][1])
			z.append(tempFaces[i][j][2])
		ax.plot(x,y,z,c='blue')
elif (choice==2):
	for i in range(0,len(tempFaces)):
		x=[]
		y=[]
		z=[]
		for j in range(0,4):
			tempFaces[i][j][0]=tempFaces[i][j][0]*matyz[0][0]+tempFaces[i][j][1]*matyz[1][0]+tempFaces[i][j][2]*matyz[2][0]
			tempFaces[i][j][1]=tempFaces[i][j][1]*matyz[0][1]+tempFaces[i][j][1]*matyz[1][1]+tempFaces[i][j][2]*matyz[2][1]
			tempFaces[i][j][2]=tempFaces[i][j][0]*matyz[0][2]+tempFaces[i][j][1]*matyz[1][2]+tempFaces[i][j][2]*matyz[2][2]
			x.append(tempFaces[i][j][0])
			y.append(tempFaces[i][j][1])
			z.append(tempFaces[i][j][2])
		ax.plot(x,y,z,c='blue')
else:
	for i in range(0,len(tempFaces)):
		x=[]
		y=[]
		z=[]
		for j in range(0,4):
			tempFaces[i][j][0]=tempFaces[i][j][0]*matxz[0][0]+tempFaces[i][j][1]*matxz[1][0]+tempFaces[i][j][2]*matxz[2][0]
			tempFaces[i][j][1]=tempFaces[i][j][1]*matxz[0][1]+tempFaces[i][j][1]*matxz[1][1]+tempFaces[i][j][2]*matxz[2][1]
			tempFaces[i][j][2]=tempFaces[i][j][0]*matxz[0][2]+tempFaces[i][j][1]*matxz[1][2]+tempFaces[i][j][2]*matxz[2][2]
			x.append(tempFaces[i][j][0])
			y.append(tempFaces[i][j][1])
			z.append(tempFaces[i][j][2])
		ax.plot(x,y,z,c='blue')

ax.set_xlabel('X')
ax.set_xlim(0,500)
ax.set_ylabel('Y')
ax.set_ylim(0,500)
ax.set_zlabel('Z')
ax.set_zlim(0,500)

plt.show()
