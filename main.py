import turtle

#screen
game_screen = turtle.Screen()
game_screen.bgcolor("white")
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
time = 30
time_table = turtle.Turtle()
time_table.hideturtle()
time_table.penup()
time_table.color("black")
time_table.goto(0,230)
time_table.write(arg= "Time: {}".format(time),align= "center", font=("Ariel", 18,"normal"))

turtle.mainloop()
