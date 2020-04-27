import time
import poly
from graphics import *

def parametric(x1,y1,x2,y2):
	
	
	if(x1>=xmin and y1>=ymin and x2<=xmax and y2<=ymax):
		line1 = Line(Point(x1,y1),Point(x2,y2))
		line1.setFill("Pink")
		line1.draw(win)
		return
		
	tLeft = 0
	tBottom = 0
	tRight = 1
	tTop = 1
	if(x2-x1 != 0):
		tLeft = -(x1-xmin)/(x2-x1)
		tRight = -(x1-xmax)/(x2-x1)
	else:
		y1 = max(y1,ymin)
		y2 = min(y2,ymax)
		line1 = Line(Point(x1,y1),Point(x2,y2))
		line1.setFill("pink")
		line1.draw(win)
		return
	if(y2-y1 != 0):
		tBottom = -(y1-ymin)/(y2-y1)
		tTop = -(y1-ymax)/(y2-y1)
	else:
		x1 = max(x1,xmin)
		x2 = min(x2,xmax)
		line1 = Line(Point(x1,y1),Point(x2,y2))
		line1.setFill("pink")
		line1.draw(win)
		return
	tE = max(0,max(tLeft,tBottom))
	tL = min(1,min(tRight,tTop))
	x1_new = x1
	y1_new = y1
	x2_new = x2
	y2_new = y2
	
	print

	if(tE == tBottom):
		y1_new = ymin
		x1_new = x1 + (x2-x1)*tE
	if(tE == tLeft):
		x1_new = xmin
		y1_new = y1 + (y2-y1)*tE
	if(tL == tRight):
		x2_new = xmax
		y2_new = y1 + (y2-y1)*tL
	if(tL == tTop):
		y2_new = ymax
		x2_new = x1 + (x2-x1)*tL
	if(x1_new>xmax or y1_new>ymax or x2_new<xmin or y2_new<ymin):
		print("Line outside range")
		return
		
	print("Line from ",x1_new,y1_new,"to",x2_new,y2_new)
	line1 = Line(Point(int(x1_new),int(y1_new)),Point(int(x2_new),int(y2_new)))
	line1.setFill("yellow")
	line1.draw(win)

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
	
points = [[100,200,100,300],[100,300,200,300],[200,300,200,200],[200,200,100,200]]
win=poly.drawPolygon(coords,points)

xmin=1000
ymin=10000
xmax=0
ymax=0

for i in range(len(points)):
	x1,y1,x2,y2 = points[i]
	xmin = min(x2,min(xmin,x1))
	xmax = max(x2,max(xmax,x1))
	ymin = min(y2,min(ymin,y1))
	ymax = max(y2,max(ymax,y1))
	
parametric(150,0,150,300)

win.getMouse()

line1 = Line(Point(150,300),Point(150,0))
line1.setFill("yellow")
line1.draw(win)

win.getMouse()
