import keyboard
import poly
import math 
from graphics import *		

def drawPolygon1(win,points):

	#points is a 2d array. each row contains (x1,y1),(x2,y2) which signifies 1 line of the polygon
	for i in range(0,len(points)):
		x1,y1,x2,y2 = points[i]
		l1 = Line(Point(x1,y1),Point(x2,y2))
		l1.setWidth(2)
		l1.setFill("yellow")
		l1.draw(win)	
	return

print("Enter 2 refrence points of line : ")
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())

del_y = (y2-y1)
del_x = (x2-x1) 
tan_thita = del_y/del_x
hyp = math.sqrt((del_y)*(del_y)+(del_x)*(del_x))
sin_thita = del_y/hyp
cos_thita = del_x/hyp
if tan_thita<0:
	cos_thita = -cos_thita


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
matrix = [[100,200,1],[100,300,1],[200,300,1],[200,200,1]]

win=poly.drawPolygon(coords,points)

def drawLine1(win):
	l2 = Line(Point(x1,y1),Point(x2,y2))
	l2.setWidth(2)
	l2.setFill("Pink")
	l2.draw(win)	
	
drawLine1(win)

def rot(win,thita):

	win.close()
	win=poly.drawPolygon(coords,points)
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	T = [[1,0,0],[0,1,0],[-x1,-y1,1]]
	for i in range(len(matrix)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += matrix[i][k] * T[k][j]
				
	T = [[cos_thita,-sin_thita,0],[sin_thita,cos_thita,0],[0,0,1]]
	result1 = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	for i in range(len(result)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result1[i][j] += result[i][k] * T[k][j]
         
        
	T = [[math.cos(thita),math.sin(thita),0],[-math.sin(thita),math.cos(thita),0],[0,0,1]]
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	for i in range(len(result1)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += result1[i][k] * T[k][j]
				
	T = [[cos_thita,sin_thita,0],[-sin_thita,cos_thita,0],[0,0,1]]
	result1 = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	for i in range(len(result)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result1[i][j] += result[i][k] * T[k][j]
	
	T = [[1,0,0],[0,1,0],[x1,y1,1]]
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
	for i in range(len(result1)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += result1[i][k] * T[k][j]
				
	temp=[]
	for i in range(len(result)):
		k = (i+1)%len(result)
		l = []
		l.append(result[i][0])
		l.append(result[i][1])
		l.append(result[k][0])
		l.append(result[k][1])
		temp.append(l)
	
	drawPolygon1(win,temp)
	drawLine1(win)
	return win
	
def shr(win,Sx,Sy):

	win.close()
	win=poly.drawPolygon(coords,points)
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	T = [[1,0,0],[0,1,0],[-x1,-y1,1]]
	for i in range(len(matrix)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += matrix[i][k] * T[k][j]
				
	T = [[cos_thita,-sin_thita,0],[sin_thita,cos_thita,0],[0,0,1]]
	result1 = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	for i in range(len(result)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result1[i][j] += result[i][k] * T[k][j]
         
        
	T = [[1,Sy,0],[Sx,1,0],[0,0,1]]	
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	for i in range(len(result1)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += result1[i][k] * T[k][j]
				
	T = [[cos_thita,sin_thita,0],[-sin_thita,cos_thita,0],[0,0,1]]
	result1 = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	for i in range(len(result)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result1[i][j] += result[i][k] * T[k][j]
	
	T = [[1,0,0],[0,1,0],[x1,y1,1]]
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
	for i in range(len(result1)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += result1[i][k] * T[k][j]
				
	temp=[]
	for i in range(len(result)):
		k = (i+1)%len(result)
		l = []
		l.append(result[i][0])
		l.append(result[i][1])
		l.append(result[k][0])
		l.append(result[k][1])
		temp.append(l)
	
	drawPolygon1(win,temp)
	drawLine1(win)
	return win

def refl(win):
	win.close()
	win=poly.drawPolygon(coords,points)
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	T = [[1,0,0],[0,1,0],[-x1,-y1,1]]
	for i in range(len(matrix)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += matrix[i][k] * T[k][j]
				
	T = [[cos_thita,-sin_thita,0],[sin_thita,cos_thita,0],[0,0,1]]
	result1 = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	for i in range(len(result)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result1[i][j] += result[i][k] * T[k][j]
         
        
	T = [[1,0,0],[0,-1,0],[0,0,1]]
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	for i in range(len(result1)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += result1[i][k] * T[k][j]
				
	T = [[cos_thita,sin_thita,0],[-sin_thita,cos_thita,0],[0,0,1]]
	result1 = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        
	for i in range(len(result)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result1[i][j] += result[i][k] * T[k][j]
	
	T = [[1,0,0],[0,1,0],[x1,y1,1]]
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
	for i in range(len(result1)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += result1[i][k] * T[k][j]
	
			
	temp=[]
	for i in range(len(result)):
		k = (i+1)%len(result)
		l = []
		l.append(result[i][0])
		l.append(result[i][1])
		l.append(result[k][0])
		l.append(result[k][1])
		temp.append(l)
	
	drawPolygon1(win,temp)
	drawLine1(win)
	return win


print("press r for rotation")
print("press f for reflection")
print("press h for shear")
print("press esc to exit")

while True:
	
	rotation = keyboard.is_pressed('r')
	reflection = keyboard.is_pressed('f')
	shear = keyboard.is_pressed('h')
	escape = keyboard.is_pressed('esc')
		
	if rotation is True:
		print("\nEnter angle by which we have to rotate : ")
		key = input()
		thita = float(input())
		win = rot(win,thita)
		rotation = False
	elif shear is True:
		print("Enter Sx : ")
		g = input()
		Sx = float(input())
		win = shr(win,Sx,0)
		shear = False
	elif reflection is True:
		g = input()
		win = refl(win)
		reflection = False
	elif escape is True:
		exit(0)
	else : continue
