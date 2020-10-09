import turtle

# setup screen from turtle

turtle.title("My Turtle Game")
turtle.bgcolor("white")
turtle.setup(600,600)
turtle.shape("turtle")

screen = turtle.Screen()
john = turtle.Turtle()

input_shape = input("What shape would you like to draw? ")
input_length = input("How big would you like your shape? ")
input_color = input("Choose a color: ")

def triangle(length, color):
    john.fillcolor(color)
    john.begin_fill()
    x = 0
    while x < 3:
        john.forward(int(length))
        john.right(120)
        x = x+1
    john.end_fill()

def star(length, color):
    john.fillcolor(color)
    john.begin_fill()
    x = 0
    while x < 5:
        john.forward(int(length))
        john.right(144)
        x = x+1
    john.end_fill()

def square(length, color):
		#john.fillcolor(color)
		#john.begin_fill()
		x = 0
		while x < 4:
			john.forward(int(length))
			john.right(90)
			x += 1
		#john.end_fill()



def shape(nsides, length):
	x = 0 
	while x < nsides:
		john.forward(int(length))
		john.right(360 / nsides)
		x += 1

def spiral(angle, growth):
	x = 0
	steps = 10
	while x < 500:
		john.forward(steps)
		john.right(angle)
		steps = steps + growth
		x = x + 1


def pattern():
	x = 0 
	while x < 1000:
		square(x, "black")
		john.right(10)
		x += 5

def spirograph(nsides, length, angle):
	for i in range(int(360 / angle)):
		shape(nsides, length)
		john.right(angle)

def rectangle(length, color):
    john.fillcolor(color)
    john.begin_fill()
    x = 0
    while x < 2:
        john.forward(int(length)*2)
        john.right(90)
        john.forward(int(length))
        john.right(90)
        x = x+1
    john.end_fill()


if input_shape == "spirograph":
	input_sides = int(input("How many sides? "))
	input_angle = int(input("What angle? "))
	spirograph(input_sides, int(input_length), input_angle)
elif input_shape == "rectangle":
	rectangle(input_length, input_color)
elif input_shape == "shape":
	input_sides = int(input("How many sides? "))
	shape(input_sides, input_length)
elif input_shape == "spiral":
	input_angle = int(input("What angle? "))
	input_growth = int(input("How much to grow each time? "))
	spiral(input_angle, input_growth)
elif input_shape == "pattern":
	pattern()
elif input_shape == "star":
	star(input_length, input_color)
elif input_shape == "triangle":	
	triangle(input_length, input_color)
elif input_shape == "square":
	square(input_length, input_color)