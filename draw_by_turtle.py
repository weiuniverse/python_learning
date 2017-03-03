import turtle


class Draw_art:
    brad = turtle.Turtle()  # initialization
    brad.shape("turtle")
    brad.color("red")
    brad.speed(1)
    def __init__(self,shape,color,speed):
        self.brad.shape(shape)
        self.brad.color(color)
        self.brad.speed(speed)

    def draw_square(self):

        #brad.forward(10)
        for step in range(4):
            self.brad.forward(100)
            self.brad.right(90)
        #brad.forward(100)
        #brad.right(90)
        #brad.forward(100)
        #brad.right(90)
        #brad.forward(100)
        #brad.right(90)

    def turn_angle(self,angle):
        self.brad.right(angle)

draw=Draw_art("turtle","red",10)
#draw.draw_square()
windows=turtle.Screen()
windows.bgcolor("yellow")
for i in range(30):
    draw.draw_square()
    draw.turn_angle(360/30)

windows.exitonclick()