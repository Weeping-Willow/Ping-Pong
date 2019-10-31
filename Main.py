import turtle

class Paddle:
    def __init__(self,x,y):
        self.paddle_0 = turtle.Turtle()
        self.paddle_0.speed(0)
        self.paddle_0.shape("square")
        self.paddle_0.color("white")
        self.paddle_0.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle_0.penup()
        self.paddle_0.goto(x,y)

#init the game
window = turtle.Screen()
window.title("Ping pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) #makes the game faster

p1 = Paddle(-350,0)

#init game loop
while True:
    window.update()