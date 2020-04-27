from graphics import *
import time
import math


def putPixle(win, x, y):
	time.sleep(0.1)
	x1,y1 = x,y
	pt = Point(x1,y1)	
	pt.draw(win)
	
def swap(x,y):
	return y,x

def drawP(xc,yc,x,y,win):
	time.sleep(0.5)
	putPixle(win,xc+x, yc+y)
	putPixle(win,xc-x, yc+y)
	putPixle(win,xc+x, yc-y)
	putPixle(win,xc-x, yc-y)
	putPixle(win,xc+y, yc+x)
	putPixle(win,xc-y, yc+x)
	putPixle(win,xc+y, yc-x)
	putPixle(win,xc-y, yc-x) 


def drawCircle(wx1,wy1,wx2,wy2,xc,yc,r):

	win = GraphWin("Circle",wx2-wx1,wy2-wy1)
	win.setCoords(wx1,wy1,wx2,wy2)


	x_axis = Line(Point(wx2,0),Point(wx1,0))	
	x_axis.draw(win)
	y_axis = Line(Point(0,wy2),Point(0,wy1))
	y_axis.draw(win)

	x = 0
	y = r
	d = 3 - 2*r
	drawP(xc,yc,x,y,win)
	while(y>=x):
		x = x+1
		if d>0:
			y = y-1
			d = d + 4*(x-y) + 10
		else:
			d = d + 4*x + 6
		drawP(xc,yc,x,y,win)

			
	

print("Enter minimum co-ordinates of window")
wx1 = int(input())
wy1 = int(input())
print("Enter maximum co-ordinates of window")
wx2 = int(input())
wy2 = int(input())

print("Enter center points")
x = int(input())
y = int(input())

print("Enter radius");
r = int(input())

drawCircle(wx1,wy1,wx2,wy2,x,y,r)

