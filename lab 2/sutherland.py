from graphics import *
import time
import poly


def x_intersect(x1,y1,x2,y2,x3,y3,x4,y4):
	num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
	den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
	return num/den
	
def y_intersect(x1,y1,x2,y2,x3,y3,x4,y4):
	num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
	den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
	return num/den

def clip(polygon,x1,y1,x2,y2):

	print(polygon)
	new_points = []
	
	for i in range(len(polygon)):
		
		k = (i+1)%(len(polygon))
		ix,iy = polygon[i]
		kx,ky = polygon[k]
		
		i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1)
		k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1)
		
		if i_pos<0 and k_pos<0:
			l = []
			l.append(kx)
			l.append(ky)
			new_points.append(l)
		elif i_pos>=0 and k_pos<0:
			l = []
			l.append(x_intersect(x1,y1, x2, y2, ix, iy, kx, ky))
			l.append(y_intersect(x1,y1, x2, y2, ix, iy, kx, ky))
			new_points.append(l)
			l = []
			l.append(kx)
			l.append(ky)
			new_points.append(l)
		elif i_pos<0 and k_pos>=0:
			l = []
			l.append(x_intersect(x1,y1, x2, y2, ix, iy, kx, ky))
			l.append(y_intersect(x1,y1, x2, y2, ix, iy, kx, ky))
			new_points.append(l)
		
	print("new_polygon =",new_points)
	polygon=[]
	for i in range(len(new_points)):
		polygon.append(new_points[i])
	return polygon
	
	
def suther(polygon):

	for i in range(len(clipper)):
		k = (i+1)%len(clipper)
		polygon = clip(polygon,clipper[i][0],clipper[i][1],clipper[k][0],clipper[k][1])
		
	for i in range(len(polygon)):
		k = (i+1)%len(polygon)
		line1 = Line(Point(polygon[i][0],polygon[i][1]),Point(polygon[k][0],polygon[k][1]))
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
	
points = [[150,150,150,200],[150,200,200,200],[200,200,200,150],[200,150,150,150]]
win=poly.drawPolygon(coords,points)

clipper = [[150,150],[150,200],[200,200],[200,150]]
polygon = [[100,150],[200,250],[300,200]]

for i in range(len(polygon)):
		k = (i+1)%len(polygon)
		line1 = Line(Point(polygon[i][0],polygon[i][1]),Point(polygon[k][0],polygon[k][1]))
		line1.setFill("white")
		line1.draw(win)

suther(polygon)

win.getMouse()

