from turtle import *
import os

#more info https://realpython.com/beginners-guide-python-turtle/#moving-the-turtle

bgcolor('black')
pensize(5)
color('green', '#98fc03')
begin_fill()
while True:
    circle(50)

    forward(150)
    color('red', '#98fc03')
    
    left(45)

    if abs(pos()) < 1:
        break
done()