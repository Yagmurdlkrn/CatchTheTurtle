import turtle

#screen
game_screen = turtle.Screen()
game_screen.bgcolor("white")
game_screen.title("Catch The Turtle")
game_screen.setup(width= 500 , height= 500)

#turtle
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.penup()
turtle_instance.speed(0)

turtle.mainloop()
