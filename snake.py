from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # this a tuple each () are different block positions that we will use to create blocks of the snake shape
UP = 90 #variable up that equals 90 that we will not change
DOWN = 270 #variable down that equals 270 that we will not change
LEFT = 180 #variable left that equals 180 that we will not change
RIGHT = 0 #variable right that equals 0 that we will not change
class Snake(Turtle): #class snake

    def __init__(self):
        super().__init__() # we grab the turtle functions that is inhereted
        self.new_blocks =[] # we will use it to store the blocks that we got from the loop below
        self.create_snake() #every time it initialize it will create a new snake that will be added to new_blocks
        self.head = self.new_blocks[0] # we add a new block behind every block that was made before
    def create_snake(self): # every time it is activate it will create the blocks making or being added to the list self.new_blocks
        for position in STARTING_POSITIONS: # this loop through our list of starting_positon and create new block for the snake body
            self.add_segment(position) #adds the new body block to the snake shape
    def add_segment(self, position):
        block = Turtle("square")  # we create the snake body
        block.color("white")  # we create the color of the snake
        block.penup()  # helps us so the user does not see the animation of the body going to it's position
        block.goto(position)  # grabs the first item in each () in the list so it can go to the x axis and make it seem like multiple body parts
        self.new_blocks.append(block)  # each body block we create get's add to a new list to store the block

    def extend(self): #extends the body of the snake
        self.add_segment(self.new_blocks[-1].position()) #we create a new block that is added behind the previous block of the snake body that is why we add [-1] in the New_blocks list which would be the last block of the list
    def move(self): # we create a method for the interlinked body part movement
    #the bottom in range loop will make the snake move forward all the time
        for new_seg in range(len(self.new_blocks) - 1, 0, - 1): #for in range loop, loops through all blocks of the snake body to move them all, it connects all the blocks movement.
            x = self.new_blocks[new_seg - 1 ].xcor() # for evert block of the snake it will let the next block to follow the first block that move. so the first block will lead the second block and so on, in regards to the x cordinates
            y = self.new_blocks[new_seg - 1 ].ycor() #it will let the next block to follow the first block that move. so the first block will lead the second block and so on, in regards to the y cordinates
            self.new_blocks[new_seg].goto(x,y) #it will apply add it to the new_blocks list, which will change the actual positons of the blocks which you will be able to see in the display screen
        self.new_blocks[0].forward(20)  #it will make the block move all the time, since block new_block[0] is the first block that will lead every other block behind it

    def up(self): #function for movement, makes the snake go up
        if self.head.heading() != DOWN: #will change the angle except if the angle was  270 before
            self.head.setheading(UP) #will change angle to 90

    def down(self): #function for movement, makes the snake go down
        if self.head.heading() != UP: #will change the angle except if the angle was  90 before
            self.head.setheading(DOWN) #will change angle to 270

    def left(self): #function for movement, makes the snake go left
        if self.head.heading() != RIGHT: #will change the angle except if the angle was 0 before
            self.head.setheading(LEFT) #will change angle to 180

    def right(self): #function for movement, makes the snake go right
        if self.head.heading() != LEFT: #will change the angle except if the angle was 180 before
            self.head.setheading(RIGHT) #will change angle to 0