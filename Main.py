import turtle

class Paddle:
    def __init__(self,x,y):
        self.x = x
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5,stretch_len=1) #stretches the with by x5 times and len by x1
        self.paddle.penup()  # removes a line thing in the middle
        self.paddle.goto(x,y) #pos of the thing
        self.score =0
    def paddle_up(self):
        y1 = self.paddle.ycor()#gets y cord
        y1+=20
        self.paddle.sety(y1) #sets y to the new value

    def paddle_down(self):
        y1 = self.paddle.ycor()  # gets y cord
        y1 -= 20
        self.paddle.sety(y1)  # sets y to the new value


class Ball:
    def __init__(self, x, y):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(x, y)
        self.dx = 0.15
        self.dy = 0.15


#init the game
window = turtle.Screen()
window.title("Ping pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) #makes the game faster

#init classes
p1 = Paddle(-350,0)
p2 = Paddle(350,0)
b1 = Ball(0,0)

#keyboard binding

window.listen()
window.onkeypress(p1.paddle_up, "w")
window.onkeypress(p1.paddle_down, "s")
window.onkeypress(p2.paddle_up, "Up")
window.onkeypress(p2.paddle_down, "Down")

#Table
table = turtle.Turtle()
table.speed(0)#animation speed
table.color("white")
table.penup()
table.hideturtle()
table.goto(0,260)
table.write("Player A: {} Player B: {}".format(p1.score,p2.score), align="center", font=("Arial", 26, "normal"))

#init game loop
while True:
    window.update()

    #ball is gonna move pog
    b1.ball.setx(b1.ball.xcor()+b1.dx)#x cord + diag x which is 0.2
    b1.ball.sety(b1.ball.ycor()+b1.dy)

    # border to keep the ball in this tyrannical game
    if b1.ball.ycor() > 290:
        b1.ball.sety(290)
        b1.dy *= -1
    if b1.ball.ycor() < -290:
        b1.ball.sety(-290)
        b1.dy *= -1
    if b1.ball.xcor() > 390:
        b1.ball.goto(0,0)
        b1.dx *= -1
        p1.score +=1
        table.clear()
        table.write("Player A: {} Player B: {}".format(p1.score, p2.score), align="center",font=("Arial", 26, "normal"))
    if b1.ball.xcor() < -390:
        b1.ball.goto(0, 0)
        b1.dx *= -1
        p2.score += 1
        table.clear()
        table.write("Player A: {} Player B: {}".format(p1.score, p2.score), align="center", font=("Arial", 26, "normal"))

    #I want to punish this terrible ball AKA it touches the paddle it goes back
    if b1.ball.xcor()<-340 and (b1.ball.ycor() < p1.paddle.ycor() + 50 and b1.ball.ycor() > p1.paddle.ycor() - 50):#
        b1.dx *=-1
    if b1.ball.xcor()>340 and (b1.ball.ycor() < p2.paddle.ycor() + 50 and b1.ball.ycor() > p2.paddle.ycor() - 50):#
        b1.dx *=-1
