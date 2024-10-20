from turtle import setup, speed, pencolor, penup, pendown, left, forward, exitonclick

# Assign canvas and shape size
canvas_size = 300
sides = 3  #edit the number of sides
side_length = 2 / sides * canvas_size

# Set the window size and turtle speed
setup(canvas_size, canvas_size)
speed(1)

# Move turtle into position
penup()
left(90)
forward(canvas_size / 3)
left(150)

# Draw a blue polygon
pencolor("blue")
pendown()
for side in range(int(sides)): 
    forward(side_length)
    left(120)

# Finished!
exitonclick()
