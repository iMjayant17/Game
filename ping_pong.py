import turtle
import winsound

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("bisque4")
wn.setup(width=800,height = 600)
wn.tracer(0)


# scores
score_a = 0
score_b = 0


# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx = 0.25
Ball.dy = 0.25


# pen for score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Blue Team : 0  Red Team : 0",align = "center",font=("courier",24,"bold"))

# functions

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")


# main game loop
while True:
    wn.update()


    # move the ball 
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border checking 
    if Ball.ycor()>290:
        Ball.sety(290)
        Ball.dy *= -1
    
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
    
    if Ball.xcor() > 390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Blue Team : {}  Red Team : {}".format(score_a,score_b),align = "center",font=("courier",24,"bold"))

    if Ball.xcor() < -390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Blue Team : {}  Red Team : {}".format(score_a,score_b),align = "center",font=("courier",24,"bold"))

    

    # paddle and the ball collision 
    if (Ball.xcor()>340 and Ball.xcor()<350) and (Ball.ycor()<paddle_b.ycor() + 40 and Ball.ycor()>paddle_b.ycor() - 40):
         Ball.setx(340)
         Ball.dx *= -1
         winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)

    if (Ball.xcor()< -340 and Ball.xcor()> -350) and (Ball.ycor()<paddle_a.ycor() + 40 and Ball.ycor()>paddle_a.ycor() - 40):
         Ball.setx(-340)
         Ball.dx *= -1
         winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)

    # paddle and the wall scheme
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)