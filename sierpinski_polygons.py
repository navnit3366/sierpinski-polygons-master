import turtle
from turtle import *
import random
import math

#Setup
turtle.speed(0)

sides = int(input('How many sides?'))
if sides < 3:
    print('Polygon must have 3 sides or more')
    exit()
detail = int(input("Level of detail from 1 to 10:"))
if detail > 10:
    print('Level of detail must be a whole number between 1 and 10')
    exit()
if detail >= 5:
    y_n = input(('High levels of detail can significantly slow down your machine. Type "YES" if you want to continue:'))
    if y_n != "YES":
        exit()
angle = float(180-((180*(sides-2))/sides))  #Calculate angles of polygon

condense_xy = []
coords_list = []
x_tri = turtle.xcor()
y_tri = turtle.ycor()

turtle.up()
turtle.goto((1000/sides)/2,200)
turtle.down()

#Draw shape
for i in range (sides):
    turtle.dot()
    x = turtle.xcor()
    y = turtle.ycor()                   
    condense_xy.extend([x, y])          #Adding each vertex to a list to be used for mdpt calculations and sierpinski formations
    coords_list.append(condense_xy)
    condense_xy =[]
    turtle.right(angle)                 
    turtle.fd(1000/sides)
turtle.up()
index_num = int((len(coords_list)) / 2)

#Determine center of shape
if (int(sides) % 2) != 0:       #Odd numbered shapes
    testmdptx = (coords_list[index_num][0] + coords_list[index_num + 1][0])/2
    testmdpty = (coords_list[index_num][1] + coords_list[index_num + 1][1])/2
    mdpt_x = (testmdptx + (coords_list[0][0]))/2
    mdpt_y = (testmdpty + (coords_list[0][1]))/2
else:                           #Even numbered shapes
    mdpt_x = (coords_list[0][0] + coords_list[index_num][0])/2
    mdpt_y = (coords_list[0][1] + coords_list[index_num][1])/2

#Draw mdpt
turtle.goto(mdpt_x, mdpt_y)
turtle.dot(size = 4)

#Iterate through triangular formations in polygons
if sides == 3:                  #Triangles only
    for i in range (1000*detail):
        pt = random.choice(coords_list)
        turtle.goto((x_tri + pt[0])/2, (y_tri + pt[1])/2)
        turtle.dot(size = 4)
        x_tri = turtle.xcor()
        y_tri = turtle.ycor()
else:       #All other polygons

    for i in range (sides):
        if i == (sides - 1):
            tri_pts = [[mdpt_x, mdpt_y]]
            tri_pts.extend([[coords_list[0][0],coords_list[0][1]]])
            tri_pts.extend([[coords_list[i][0],coords_list[i][1]]])
            for j in range (math.floor((1000*detail)/sides)):
                pt = random.choice(tri_pts)
                turtle.goto((x_tri + pt[0])/2, (y_tri + pt[1])/2)
                turtle.dot(size = 4)
                x_tri = turtle.xcor()
                y_tri = turtle.ycor()
        else:
            tri_pts = [[mdpt_x, mdpt_y]]
            x_tri = mdpt_x
            y_tri = mdpt_y
            tri_pts.extend([[coords_list[i][0],coords_list[i][1]]])
            tri_pts.extend([[coords_list[i+1][0],coords_list[i+1][1]]])
            for j in range (math.floor((1000*detail)/sides)):
                pt = random.choice(tri_pts)
                turtle.goto((x_tri + pt[0])/2, (y_tri + pt[1])/2)
                turtle.dot(size = 4)
                x_tri = turtle.xcor()
                y_tri = turtle.ycor()
print('Done')
done()