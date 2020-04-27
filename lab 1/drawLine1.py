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


def drawLine(wx1,wx2,wy1,wy2,x0,y0,x1,y1):

	win = GraphWin("Line",wx2-wx1,wy2-wy1)
	win.setCoords(wx1,wy1,wx2,wy2)


	x_axis = Line(Point(wx2,0),Point(wx1,0))	
	x_axis.draw(win)
	y_axis = Line(Point(0,wy2),Point(0,wy1))
	y_axis.draw(win)

	
	dx = abs(x1 - x0)
	dy = abs(y1 - y0)
	slope = 0
	if(dx==0):
		x2,y2 = x0,y0
		x3,y3 = x1,y1
		l1 = Line(Point(x2,y2),Point(x3,y3))
		l1.setWidth(2)
		l1.draw(win)
		time.sleep(5)
		return
	else:	
		slope = dy/float(dx)

	x, y = x0, y0
	if slope > 1:
	    dx, dy = dy, dx
	    x, y = y, x
	    x0, y0 = y0, x0
	    x1, y1 = y1, x1
	p = 2 * (dy - dx)
	putPixle(win, x, y)
	for k in range(2, dx):
	    if p > 0:
	        y = y + 1 if y < y1 else y - 1
	        p = p + 2*(dy - dx)
	    else:
	        p = p + 2*dy
	    x = x + 1 if x < x1 else x - 1
	    putPixle(win, x, y)	
	time.sleep(30)		
	

print("Enter minimum co-ordinates of window")
wx1 = int(input())
wy1 = int(input())
print("Enter maximum co-ordinates of window")
wx2 = int(input())
wy2 = int(input())

print("Enter points")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

drawLine(wx1,wx2,wy1,wy2,x1,y1,x2,y2)

