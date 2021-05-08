import turtle as t
import random
playerAscore=0
playerBscore=0


#window

window = t.Screen()
window.title("Pong Game")
window.bgcolor('black')
window.setup(width=800,height=600)
window.tracer(0) #to set speed of window

#creating left paddle

leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color('white')
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#creating right paddle

rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color('white')
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#ball
ball=t.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(0,0)
ballxdirection=0.5
ballydirection=0.5

#pen for score board
pen=t.Turtle()
pen.penup()
pen.goto(0,250)
pen.speed(0)
pen.color("blue")
pen.hideturtle()
pen.write("score",align="center",font=('Arial',20,'normal'))

#moving left paddle

def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)

#moving right paddle

def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)

def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)

#listen to action
window.listen()
window.onkeypress(leftpaddleup,"w")
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,"Up")
window.onkeypress(rightpaddledown,'Down')

# Main loop
while True:
  window.update() # Update window
  #to move ball
  ball.setx(ball.xcor()+ballxdirection)
  ball.sety(ball.ycor()+ballydirection)

  #set borders
  if ball.ycor()>290:
      ball.sety(290)
      ballydirection=ballydirection*-1
  if ball.ycor()<-290:
      ball.sety(-290)
      ballydirection=ballydirection*-1
  if ball.xcor()>390:
      ball.goto(0,0)
      ballydirection = 0.5
      ballxdirection = 0.5
      playerAscore=playerAscore+1
      pen.clear()
      pen.write("playerA:{}  playerB:{}".format(playerAscore,playerBscore),align='center',font=('Arial',20,'normal'))
  if ball.xcor() < -390:
      ball.goto(0, 0)
      ballydirection = 0.5

      ballxdirection = -0.5
      playerBscore = playerBscore + 1
      pen.clear()
      pen.write("playerA:{}  playerB:{}".format(playerAscore, playerBscore), align='center',font=('Arial', 20, 'normal'))
  if ((ball.xcor() > 340 and ball.xcor() < 350) and (rightpaddle.ycor() - 60 < ball.ycor() and ball.ycor() < rightpaddle.ycor() + 60)):
      ball.setx(340)
      ballxdirection = ballxdirection * -1.2
      ballydirection = ballydirection*random.uniform(-1.0,1.0)
  if ((ball.xcor() < -340 and ball.xcor() > -350) and (leftpaddle.ycor() - 60 < ball.ycor() and ball.ycor() < leftpaddle.ycor() + 60)):
      ball.setx(-340)
      ballxdirection = ballxdirection * -1.2
      ballydirection = ballydirection * random.uniform(-1.0, 1.0)
