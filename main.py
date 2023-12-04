import turtle
import random
import time


#screen
game_screen = turtle.Screen()
game_screen.bgcolor("light blue")
game_screen.title("Catch The Turtle")
game_screen.setup(width= 600 , height= 600)

#turtle
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.penup()
turtle_instance.speed(0)

#score
score = 0
score_table = turtle.Turtle()
score_table.hideturtle()
score_table.penup()
score_table.color("black")
score_table.goto(0,260)
score_table.write(arg= "Score: {}".format(score),align= "center", font=("Ariel", 20, "normal"))

#time
countdown = 30
time_table = turtle.Turtle()
time_table.hideturtle()
time_table.penup()
time_table.color("black")
time_table.goto(0,230)
time_table.write(arg= "Time: {}".format(countdown),align= "center", font=("Ariel", 18,"normal"))

def turtle_location():
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    turtle_instance.goto(x,y)

def turtle_score():
    score_table.clear()
    score_table.write(arg= "Score: {}".format(score),align= "center", font=("Ariel", 20, "normal"))

def turtle_time():
    global countdown
    countdown -= 1
    time_table.clear()
    time_table.write(arg="Time: {}".format(countdown), align="center", font=("Ariel", 18, "normal"))
    if countdown <= 0:
        time_table.clear()
        time_table.write(arg="Game Over", align="center", font=("Ariel", 18, "normal"))
        turtle_instance.hideturtle()
    else:
        turtle_location()

def turtle_click(x,y):
    global score
    turtle_location()
    score += 1
    turtle_score()


game_screen.onclick(turtle_click)

while countdown > 0:
    turtle_time()
    time.sleep(1)


turtle.mainloop()
