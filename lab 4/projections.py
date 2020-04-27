import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from math import *


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
	
def orthographic():
	
	for i in range(0,len(faces)):
		x=[]
		y=[]
		z=[]
		for j in range(0,4):
			x.append(faces[i][j][0])
			y.append(faces[i][j][1])
			z.append(faces[i][j][2])
			
		ax.plot(x,y,z,c="red")

	print(" Orthographic Parallel projects ")
	print("Select principle plane (xy->1 or yz->2 or xz->3) Enter number :")
	k = int(input())


	if k==1:
		for i in range(0,len(tempFaces)):
			for j in range(0,4):
				tempFaces[i][j][2]=0

	elif k==2:
		for i in range(0,len(tempFaces)):
			for j in range(0,4):
				tempFaces[i][j][0]=0

	else:
		for i in range(0,len(tempFaces)):
			for j in range(0,4):
				tempFaces[i][j][1]=0
				
	for i in range(0,len(tempFaces)):
		x=[]
		y=[]
		z=[]
		for j in range(0,4):
			x.append(tempFaces[i][j][0])
			y.append(tempFaces[i][j][1])
			z.append(tempFaces[i][j][2])
			
		ax.plot(x,y,z,c="blue")
		
def axonometric():
	
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
		
def isometric():

	print(" isometric projections ")
	n1=1
	n2=1
	n3=1
	a=-1
	b=-1
	c=-1
	R0=[0,0,0]
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
		
def dimetric():
	
	print(" dimetric projections ")
	n1=1
	n2=1
	n3=2
	a=-1
	b=-1
	c=-2
	R0=[0,0,0]
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

def trimetric():
	
	print(" trimetric projections ")
	n1=1
	n2=2
	n3=3
	a=-1
	b=-2
	c=-3
	R0=[0,0,0]
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
		
def perspective():
	
	print(" Perspective  projections ")
	print("Enter vector normal :")
	n1=int(input())
	n2=int(input())
	n3=int(input())
	print("Enter reference point :")
	R0=input().split()
	print("Enter projectors coordinates a,b,c")
	a=int(input())
	b=int(input())
	c=int(input())

	d0=int(R0[0])*n1+int(R0[1])*n2+int(R0[2])*n3
	d1=a*n1+b*n2+c*n3
	d=d0-d1


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
			x0=(x0*(a*n1+d)+y0*a*n2+z0*a*n3-a*(d1+d))/(x0*n1+y0*n2+z0*n3-d1)
			y0=(y0*(b*n2+d)+x0*b*n1+z0*b*n3-b*(d1+d))/(x0*n1+y0*n2+z0*n3-d1)
			z0=(z0*(c*n3+d)+y0*c*n2+x0*c*n1-c*(d1+d))/(x0*n1+y0*n2+z0*n3-d1)
			tempFaces[i][j][0]=x0
			tempFaces[i][j][1]=y0
			tempFaces[i][j][2]=z0
			x.append(x0)
			y.append(y0)
			z.append(z0)
		ax.plot(x,y,z,c='blue')
		
def cabinet():
	
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


def cavalier():

	print("Cavalier projections ")
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

	matxy=[[1,0,0],[0,1,0],[0.5*cos(radians(45)),0.5*sin(radians(45)),0]]
	matyz=[[0,1,0],[0,0,1],[0,0.5*cos(radians(45)),0.5*sin(radians(45))]]
	matxz=[[0,0,1],[1,0,0],[0.5*cos(radians(45)),0,0.5*sin(radians(45))]]
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
	

print("Enter choice: Orthographic->'o'	Axonometric->'a' Isometric->'i' Dimetric->'d' trimetri->'t' Perspective->'p' cabinet->'c' cavalier->'v'")
choice = input()

if choice=='o':
	orthographic()
elif choice=='a':
	axonometric()
elif choice=='i':
	isometric()
elif choice=='d':
	dimetric()
elif choice=='t':
	trimetric()
elif choice=='p':
	perspective()
elif choice=='c':
	cabinet()	
elif choice=='v':
	cavalier()
	
ax.set_xlabel('X')
ax.set_xlim(0,500)
ax.set_ylabel('Y')
ax.set_ylim(0,500)
ax.set_zlabel('Z')
ax.set_zlim(0,500)

plt.show()

