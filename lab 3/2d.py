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


coords = [-500,-500,500,500]
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

def trans(win,Tx,Ty):
	win.close()
	win=poly.drawPolygon(coords,points)
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
	T = [[1,0,0],[0,1,0],[Tx,Ty,1]]
	for i in range(len(matrix)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += matrix[i][k] * T[k][j]
				
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
	return win

def rot(win,thita):
	win.close()
	win=poly.drawPolygon(coords,points)
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
	T = [[math.cos(thita),math.sin(thita),0],[-math.sin(thita),math.cos(thita),0],[0,0,1]]
	print(T)
	for i in range(len(matrix)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += matrix[i][k] * T[k][j]
				
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
	return win

def scal(win,Sx,Sy):
	win.close()
	win=poly.drawPolygon(coords,points)
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
	T = [[Sx,0,0],[0,Sy,0],[0,0,1]]
	for i in range(len(matrix)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += matrix[i][k] * T[k][j]
				
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
	return win
	
def shr(win,Sx,Sy):
	win.close()
	win=poly.drawPolygon(coords,points)
	result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
	T = [[1,Sy,0],[Sx,1,0],[0,0,1]]
	for i in range(len(matrix)):
		for j in range(len(T[0])):
			for k in range(len(T)):
				result[i][j] += matrix[i][k] * T[k][j]
				
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
	return win



print("press t for translation")
print("press r for rotation")
print("press s for scaling")
print("press f for reflection")
print("press h for shear")
print("press esc to exit")

while True:
	
	translation = keyboard.is_pressed('t')
	rotation = keyboard.is_pressed('r')
	scaling = keyboard.is_pressed('s')
	reflection = keyboard.is_pressed('f')
	shear = keyboard.is_pressed('h')
	escape = keyboard.is_pressed('esc')
	
	if translation is True:
		print("\nEnter Tx abd Ty :")
		key = input()
		Tx = float(input())
		Ty = float(input())
		win = trans(win,Tx,Ty)
		translation = False
	elif rotation is True:
		print("\nEnter angle by which we have to rotate : ")
		key = input()
		thita = float(input())
		win = rot(win,thita)
		rotation = False
	elif scaling is True:
		print("\nEnter Sx and Sy :")
		key = input()
		Sx = float(input())
		Sy = float(input())
		win = scal(win,Sx,Sy)
		scaling = False
	elif shear is True:
		print("\nEnter axis in which shearing is to be done")
		x = input()
		if x=='x':
			print("Enter Sx : ")
			Sx = float(input())
			win = shr(win,Sx,0)
		else:
			print("Enter Sy: ")
			Sy = float(input())
			win = shr(win,0,Sy)
		shear = False
	elif escape is True:
		exit(0)
	else : continue
