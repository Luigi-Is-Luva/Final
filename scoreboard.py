from turtle import Turtle # we get the Turtle class
ALIGNMENT = "center" # aligment positon is called center according to systax of align
FONT = ("Courier", 24, "normal") #font  attributes (name, size, type)

class Scoreboard(Turtle): #inherentence the Turtle class from turtle library

    def __init__(self): #initialize function every time class is used
        super().__init__() #makes the turtle library function avaliable from Turtle
        self.score = 0 #initial score
        self.color("white") #color of the scoreboard
        self.penup() #makes it so we do not see it go to position
        self.goto(0,270) #gives it position
        self.hideturtle() #hides the turtle shape
        self.update_scoreboard() #updates the scoreboard at the end of the __init__ function

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT) #write the scorem aligns it, gives it the font

    def game_over(self): #every time it activate it shows game over in the screen
        self.goto(0, 0) #positions of the words
        self.write("Game Over", align =ALIGNMENT, font= FONT ) # shows (text, alignment 'center' and fonty attributes
    def increase_score(self):
        self.score += 1 #increases socre by one everytime it is used, returns it to self.score on the __init__ function
        self.clear()   #clears word of previous score
        self.update_scoreboard() #gives the score to self.write in update_scoreboard