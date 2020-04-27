#orthographic parallel projection
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



ax.set_xlabel('X')
ax.set_xlim(0,500)
ax.set_ylabel('Y')
ax.set_ylim(0,500)
ax.set_zlabel('Z')
ax.set_zlim(0,500)

plt.show()
