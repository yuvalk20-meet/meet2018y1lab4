import turtle # python needs this to use all the turtle functions
'''
turtle.shape('turtle') # changes the shape to a turtle
finn = turtle.clone() # creates new turtle and saves it in finn
finn.shape('square') # changes shape of 2nd turtle to square
finn.goto(100,0) # moves square to (x=100,y=100)
finn.goto(100, 100)
finn.goto(0, 100)
finn.goto(0,0)
'''

turtle.shape('arrow')
charlie = turtle.clone()
charlie.goto(50,0)
charlie.shape('blank')
charlie.goto(100,0)
charlie.shape('blank')
charlie.left(45)
charlie.goto(50,50)
charlie.shape('circle')
charlie.goto(100,50)
charlie.shape('classic')
charlie.right(45)
charlie.goto(0,50)
charlie.shape('square')
charlie.goto(0,0)
