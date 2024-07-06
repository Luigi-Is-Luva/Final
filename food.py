from turtle import Turtle #grabs the Turtle class from the turtle lib
import random #import random module

class Food(Turtle): #inherentence turtle library to our FOod class

    def __init__(self):
        super().__init__() # makes us able to start using turtle class, that's why we add super()
        self.shape("circle") #shape of the food
        self.penup()   #makes it so we can not see it moves
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #make the food circle change width and legnth
        self.color("blue") #color of the food circle
        self.speed("fastest") # changes how quick is spawn
        self.refresh() #spawns random coordinates for the food every time function is initialized

    def refresh(self): # when function is used it is return to the original function __init__
        random_x = random.randint(-280, 280) #grabs a x random coordinate from the display length and width
        random_y = random.randint(-280, 280) #grabs a y random coordinate from the display length and width
        self.goto(random_x, random_y) #combines the 2 previous coordinates and return coordinates to original __init__
