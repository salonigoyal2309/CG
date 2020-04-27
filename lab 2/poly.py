from graphics import *
arr = [[0 for i in range(800)] for j in range(800)] 

def putPixle1(win, x, y):
	#time.sleep(0.1)
	x1,y1 = x,y
	arr[x][y]=1;
	pt = Point(x1,y1)	
	pt.draw(win)
	pt.setFill("white")
	
def swap(x,y):
	return y,x
	
	
def drawLine(win,coords,x0,y0,x1,y1):
	
	dx = x1 - x0
	dy = y1 - y0
	
	if(dx==0):
		x2,y2 = x0,y0
		x3,y3 = x1,y1
		l1 = Line(Point(x2,y2),Point(x3,y3))
		l1.setWidth(2)
		l1.setFill("white")
		l1.draw(win)
		return
	elif dx > 0:
		xsign = 1
	else:
		xsign = -1
	if dy > 0:
		ysign = 1
	else:
		ysign = -1

	dx = abs(dx)
	dy = abs(dy)
	
	if dx > dy: #slope<1 since x is always incrementing
		xx=xsign
		xy=0
		yx=0
		yy =ysign
	else: #slope>1 since y is always incrementing
		dx, dy = dy, dx
		xx=0
		xy=ysign
		yx=xsign
		yy=0

	D = 2*dy - dx
	y = 0

	for x in range(dx + 1):
		putPixle1(win,x0 + x*xx + y*yx, y0 + x*xy + y*yy)
		if D >= 0: #North-East is chosen
			y += 1
			D -= 2*dx
		D += 2*dy #East is chosen	
	
					
		

def drawPolygon(coords,points):
	#points is a 2d array. each row contains (x1,y1),(x2,y2) which signifies 1 line of the polygon
	wx1,wy1,wx2,wy2 = coords
	win = GraphWin("Line",wx2-wx1,wy2-wy1)
	ar = [[0]*(wx2-wx1)]*(wy2-wy1)
	win.setBackground("black")
	win.setCoords(wx1,wy1,wx2,wy2)
	x_axis1x,x_axis1y = wx2,0
	x_axis2x,x_axis2y = wx1,0
	y_axis1x,y_axis1y = 0,wy2
	y_axis2x,y_axis2y = 0,wy1
	x_axis = Line(Point(x_axis1x,x_axis1y),Point(x_axis2x,x_axis2y))
	x_axis.draw(win)
	x_axis.setFill("white")
	y_axis = Line(Point(y_axis1x,y_axis1y),Point(y_axis2x,y_axis2y))
	y_axis.draw(win)
	y_axis.setFill("white")

	for i in range(0,len(points)):
		x1,y1,x2,y2 = points[i]
		drawLine(win,coords,x1,y1,x2,y2)
		
	win.getMouse()
	return win	
	
	
#print("Enter minimum co-ordinates of window")
#wx1 = int(input())
#wy1 = int(input())
#print("Enter maximum co-ordinates of window")
#wx2 = int(input())
#wy2 = int(input())
#print("Enter minimum co-ordinates of viewport")
#vx1 = int(input())
#vy1 = int(input())
#print("Enter maximum co-ordinates of viewport")
#vx2 = int(input())
#vy2 = int(input())
#coords = [-400,-500,500,500]

#print("Enter lines in the polygon")
#x = int(input())

#points=[]

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

#drawPolygon(coords,points)
