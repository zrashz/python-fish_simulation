import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Fish Tank Simulation")
wn.setup(width=800, height=600)
wn.tracer(0)  # Disable automatic screen updates for smoother animation

# Create a custom fish shape
def create_fish_shape():
    fish = turtle.Turtle()
    fish.penup()
    fish.hideturtle()
    fish.speed(0)
    fish.begin_poly()

    # Drawing a simple fish-like shape
    fish.forward(10)    # Body
    fish.left(120)
    fish.forward(20)
    fish.left(120)
    fish.forward(20)
    fish.left(120)
    fish.forward(10)
    fish.right(60)      # Tail
    fish.forward(10)
    fish.right(120)
    fish.forward(10)
    fish.right(120)
    fish.forward(10)

    fish.end_poly()
    fish_shape = fish.get_poly()
    wn.register_shape("fish", fish_shape)

# Register the fish shape
create_fish_shape()

# Create a fish class
class Fish(turtle.Turtle):
    def __init__(self, color, size, speed, direction):
        super().__init__()
        self.shape("fish")  # Custom fish shape
        self.color(color)
        self.shapesize(stretch_wid=size, stretch_len=size * 2)  # Stretch to resemble fish
        self.penup()
        self.goto(random.randint(-390, 390), random.randint(-290, 290))
        self.setheading(direction)  # Fish moves in the given direction
        self.speed_factor = speed

    def move(self):
        self.forward(self.speed_factor)
        
        # Boundary checking: Reverse direction if hitting the boundaries
        if self.xcor() > 390 or self.xcor() < -390:
            self.setheading(180 - self.heading())  # Reverse direction left-right
        if self.ycor() > 290 or self.ycor() < -290:
            self.setheading(360 - self.heading())  # Reverse direction up-down

# Create multiple fish with varying directions (left-right and top-bottom)
fishes = []
colors = ["red", "yellow", "green", "purple", "orange", "cyan"]
for _ in range(20):  # Create 20 fish
    direction = random.choice([0, 90, 180, 270])  # Fish moves in one of four directions
    fish = Fish(random.choice(colors), random.uniform(0.5, 1.5), random.uniform(1, 3), direction)
    fishes.append(fish)

# Main loop
while True:
    for fish in fishes:
        fish.move()
    wn.update()  # Update the screen manually

# Close the window when clicked
wn.mainloop()
