from turtle import*
from random import*

sc = Screen()
sc.bgcolor('black')

score = 0

border = Turtle()
border.speed(0)
border.color('red')
border.goto(-300, -260)
border.hideturtle()

for i in range(1):
    border.clear()
    border.goto(-300, 260)
    border.goto(300, 260)
    border.goto(300, -260)
    border.goto(-300, -260)

pen = Turtle()
pen.speed(0)
pen.penup()
pen.color('red')
pen.goto(0, 260)
pen.hideturtle()
pen.write('Score: {}'.format(score), align = 'center', font = ('Courier', 24, 'normal'))

class Player(Turtle):
    def __init__(self, speed, color, shape):
        super().__init__()
        self.speed(speed)
        self.penup()
        self.color(color)
        self.shape(shape)

    def Forward(self):
        move = self.xcor()
        move += 10
        self.setx(move)
        if self.xcor() > 300:
            self.setx(300)

    def Backward(self):
        move = self.xcor()
        move -= 10
        self.setx(move)
        if self.xcor() < -300:
            self.setx(-300)

    def Up(self):
        move = self.ycor()
        move += 10
        self.sety(move)
        if self.ycor() > 260:
            self.sety(260)

    def Down(self):
        move = self.ycor()
        move -= 10
        self.sety(move)
        if self.ycor() < -260:
            self.sety(-260)

class Enemy(Turtle):
    def __init__(self, speed, color, shape):
        super().__init__()
        self.speed(speed)
        self.penup()
        self.color(color)
        self.shape(shape)

    def Enemy_move(self):
        self.forward(1)

player = Player(0, 'red', 'square')
enemy = Enemy(0, 'white', 'circle')
enemy.goto(randint(-300, 300), randint(-260, 260))

listen()
onkey(player.Forward, 'd')
onkey(player.Backward, 'a')
onkey(player.Up, 'w')
onkey(player.Down, 's')

while True:
    sc.update()
    
    enemy.Enemy_move()

    if enemy.xcor() > 300 or enemy.xcor() < -300 and enemy.ycor() > 260 or enemy.ycor() < -260:
        enemy.goto(randint(-300, 300), randint(-260, 260))

    if player.distance(enemy) < 16:
        enemy.goto(randint(-300, 300), randint(-260, 260))
        pen.clear()
        score += 1
        pen.write('Score: {}'.format(score), align = 'center', font = ('Courier', 24, 'normal'))

sc.mainloop()