import poly
from graphics import *

fill = [[0 for i in range(800)] for j in range(800)] 

def fill4(win,coords):

	#print(ar[0])
	
	x,y = 0,0
	stack = []
	stack.append([x,y])
	
	
	while len(stack)!=0:
	
		x,y = stack[len(stack)-1][0],stack[len(stack)-1][1]
		stack.pop()
		print(x,y,poly.arr[x][y])

		if x>400 or x<-400 or y>400 or y<-400 :
			continue;


		if poly.arr[x][y]==0:
			pt = Point(x,y)	
			pt.draw(win)
			pt.setFill("yellow")
			fill[x][y]=1
		else: continue
		
		if fill[x+1][y]==0 and poly.arr[x+1][y]==0:
			stack.append((x+1,y))
				
		if fill[x][y+1]==0 and poly.arr[x][y+1]==0:
			stack.append((x,y+1))
			
		if fill[x-1][y]==0 and poly.arr[x-1][y]==0:
			stack.append((x-1,y))
			
		if fill[x][y-1]==0 and poly.arr[x][y-1]==0:
			stack.append((x,y-1))


coords = [-400,-400,400,400]
points=[]

#for i in range(0,x):
	#crd=[]
	#print("Enter coordinates of line",i)
	#x0 = int(input())
	#y0 = int(input())
	#x1 = int(input())
	#y1 = int(input())
	#crd.append(x0)
	#crd.append(y0)
	#crd.append(x1)
	#crd.append(y1)
	#points.append(crd)
	
points=[[-100,-100,0,100],[0,100,100,-100],[100,-100,-100,-100]]
win=poly.drawPolygon(coords,points)
fill4(win,coords)
