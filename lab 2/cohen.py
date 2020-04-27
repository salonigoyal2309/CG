from graphics import *
import time
import poly

INSIDE = 0 
LEFT = 1    
RIGHT = 2   
BOTTOM = 4  
TOP = 8     

def computeCode(x, y): 
    code = INSIDE 
    if x < xmin:     
        code |= LEFT 
    elif x > xmax:   
        code |= RIGHT 
    if y < ymin:     
        code |= BOTTOM 
    elif y > ymax:    
        code |= TOP 
  
    return code 
    
def cohen(x1,y1,x2,y2):

	code1 = computeCode(x1, y1)
	code2 = computeCode(x2, y2)
	accept = False
	done = False
	while True:
		if code1 == 0 and code2 == 0:
			accept = True
			break
		elif (code1 & code2) != 0:
			done = True
			break
		else:
			x= 1.0
			y = 1.0
			if code1 != 0:
				code_out = code1
			else:
				code_out = code2
			if code_out & TOP:
				x = x1 + (x2 - x1) *(ymax - y1) / (y2 - y1)
				y= ymax
			elif code_out & BOTTOM:
				x = x1 + (x2 - x1) *(ymin - y1) / (y2 - y1)
				y = ymin
			if code_out & RIGHT:
				y = y1 + (y2 - y1) *(xmax - x1) / (x2 - x1)
				x = xmax
			elif code_out & LEFT:
				y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
				x = xmin
			if code_out == code1:
				x1 = x
				y1 = y
				code1 = computeCode(x1,y1)
			else:
				x2 = x
				y2 = y
				code2 = computeCode(x2, y2)
	if accept:
		print ("Line : %.2f,%.2f to %.2f,%.2f" % (x1,y1,x2,y2))
		line1 = Line(Point(x1,y1),Point(x2,y2))
		line1.setFill("Pink")
		line1.draw(win)
	else:
		print("Line rejected") 
  


	
	
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
	
cohen(-200,-200,200,300)

win.getMouse()

line1 = Line(Point(-200,-200),Point(200,300))
line1.setFill("yellow")
line1.draw(win)

win.getMouse()

