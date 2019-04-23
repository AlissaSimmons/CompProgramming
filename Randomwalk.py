"""

Project 5 Random Walk
Alissa
Period A1 Computer Programming 1
Random walk demonstrates the pseudorandom number generator as well as displacement vs distance
"""
#import statements
import math,pygame,random
#variable and setup
screen = pygame.display.set_mode((1200,800))
    #declare starting x and y
x = screen.get_width()1/2
y = screen.get_height()1/2
    #declare a list of points
points = []
points.append((x,y))
    #declare a number to represent how many steps
steps = int(input("How many randum unbalanced steps will you be taking?"))
stepsTaken = 0
done = False
#constants

#functions

#main progress
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if stepsTaken <= steps:
        #generate a random angle

        # Option #2 store tempx and tempy
        tempx = x
        tempy = y

        #calculate the x component
        
        # calculate the y component
    
        
        #Option #1 append the new point to the points list
        points.append((x,y))
        
        # increment the stepsTaken

        # draw the new line representing the steps
    pygame.display.flip()