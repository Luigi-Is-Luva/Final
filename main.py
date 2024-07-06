from turtle import Screen #from the turtle library we get the screen class
import time #import the time library function
from snake import Snake #from the snake.py file we get the Snake class
from food import Food #from the food.py we get the FOod class
from scoreboard import Scoreboard #from the scoreboard.py we get the Scoreboard class


screen = Screen() #showcase a display screen so i can see the animations
screen.setup(width=600, height=600) #gives me the setup of width and height of my displau screen
screen.bgcolor("black") #makes my display screen color black
screen.title("Snake") #Gives a title to my display screen
screen.tracer(0) #the first second animation is skipped so you see it start when all the blocks of the snake are in position

snake = Snake() #gets the Snake.py class with thiere methods
food = Food() # i set the Food() class from food,py to food
scoreboard = Scoreboard() #scoreboard class gets added from scoreboard.py

screen.listen() #this .listen function will help the screen listen to our keeyboard clicks
screen.onkey(snake.up, "Up") #if i press the up arrow key it go up
screen.onkey(snake.down, "Down") #if i press the down arrow key it go down
screen.onkey(snake.left, "Left") #if i press the left arrow key it go left
screen.onkey(snake.right, "Right") #if i press the right arrow key it go right

game = True # helps us create a loop that will stop unless certain conditions are meet
while game: # while loop
    screen.update() #helps us make the snake seem like they are updating together and not one by one when it comes to each body part
    time.sleep(0.1) #helps how quick the animation is going to longer the int the slower it is, it delays after all 3 segmente are done

    snake.move() #uses the Snake move method which just makes the snake move forword as long as game is true in the while loop

     #Detect collision with food
    if snake.head.distance(food) < 15: #it the distance bewteen the food is less than 15 then a new food gets spwan
        food.refresh() #new food circle is generate
        snake.extend() #extends the body of the snake once it's close to the food
        scoreboard.increase_score() #every time it gets less than 15 then the scoreboard score increase

        #detects collision with wall of the display width and height, if it hits one of the 2 the game ends
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game= False #game ends
        scoreboard.game_over() #the screen shows 'game over' when it hit the walls


    #Detch collision with tail
    for segment in snake.new_blocks:
        if segment == snake.head:  #if the segment is the head it does not count
            pass #pass the function until it hits it's body
        elif snake.head.distance(segment) < 10: #if the snake hit's it own segments aka blocks of it's body the game ends
            game= False #game ends
            scoreboard.game_over() #text showing game is over
screen.exitonclick() #this function helps us make the  display show unless i click it