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


def drawEllipse(wx1,wy1,wx2,wy2,xc,yc,rx,ry):

	win = GraphWin("Circle",wx2-wx1,wy2-wy1)
	win.setCoords(wx1,wy1,wx2,wy2)


	x_axis = Line(Point(wx2,0),Point(wx1,0))	
	x_axis.draw(win)
	y_axis = Line(Point(0,wy2),Point(0,wy1))
	y_axis.draw(win)

	x = 0
	y = ry
	p = (ry*ry) - (rx*rx*ry) + ((rx*rx)/4)
	while((2*x*ry*ry) < (2*y*rx*rx)):
		putPixle(win,xc+x,yc-y)
		putPixle(win,xc-x,yc+y)
		putPixle(win,xc+x,yc+y)
		putPixle(win,xc-x,yc-y)
		if(p<0):
			x = x+1
			p = p + (2*ry*ry*x) + (ry*ry)
		else:
			x = x+1
			y = y-1
			p = p + (2*ry*ry*x + ry*ry) - (2*rx*rx*y)

	p = (float(x) + 0.5)*(float(x)+0.5)*ry*ry + (y-1)*(y-1)*rx*rx - rx*rx*ry*ry
	while(y>=0):
		putPixle(win,xc+x,yc-y)
		putPixle(win,xc-x,yc+y)
		putPixle(win,xc+x,yc+y)
		putPixle(win,xc-x,yc-y)
		if(p>0):
			y = y-1
			p = p - (2*rx*rx*y) + (rx*rx)
		else:
			y = y-1
			x = x+1
			p = p + (2*ry*ry*x) - (2*rx*rx*y) - (rx*rx)


			
	

print("Enter minimum co-ordinates of window")
wx1 = int(input())
wy1 = int(input())
print("Enter maximum co-ordinates of window")
wx2 = int(input())
wy2 = int(input())

print("Enter center points")
x = int(input())
y = int(input())

print("Enter radius 1")
r1 = int(input())

print("Enter radius 2")
r2 = int(input())

drawEllipse(wx1,wy1,wx2,wy2,x,y,r1,r2)

