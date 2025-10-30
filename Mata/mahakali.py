import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("navy")  # Dark blue background like night sky
screen.setup(800, 600)
screen.title("Shubh Dusshera 2022")

# Create turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.hideturtle()

def draw_diya(x, y, size):
    """Draw a traditional diya (oil lamp)"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Diya base - golden yellow
    t.color("#FFD700")  # Gold color
    t.begin_fill()
    for _ in range(2):
        t.forward(size)
        t.left(90)
        t.forward(size//3)
        t.left(90)
    t.end_fill()
    
    # Flame - kumkuma red to yellow gradient effect
    t.penup()
    t.goto(x + size//2, y + size//3)
    t.pendown()
    t.color("#FF6B35")  # Orange-red
    t.begin_fill()
    t.circle(size//6)
    t.end_fill()

def draw_flower(x, y, size, color):
    """Draw a decorative flower"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    
    t.begin_fill()
    for _ in range(8):
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(60)
    t.end_fill()

def draw_ornamental_border():
    """Draw traditional Indian border"""
    colors = ["#FFD700", "#FF6B35", "#4CAF50", "#E91E63"]
    t.penup()
    t.goto(-350, -250)
    t.pendown()
    t.width(3)
    
    for i in range(4):
        t.color(colors[i % len(colors)])
        for _ in range(5):
            t.forward(40)
            t.circle(10, 180)
        t.left(90)

def write_text():
    """Write Dusshera greetings"""
    # Main title
    t.penup()
    t.goto(0, 150)
    t.color("#FFD700")  # Gold
    t.write("शुभ दशहरा", align="center", font=("Arial", 40, "bold"))
    
    # Subtitle
    t.goto(0, 100)
    t.color("#FF6B35")  # Kumkuma red
    t.write("Happy Dusshera 2024", align="center", font=("Arial", 24, "normal"))
    
    # Blessings
    blessings = [
        "जय माँ दुर्गा",
        "Victory of Good over Evil",
        "May Goddess Durga bless you",
        "with happiness and prosperity"
    ]
    
    t.goto(0, 50)
    t.color("#4CAF50")  # Green
    for i, blessing in enumerate(blessings):
        t.goto(0, 50 - i*30)
        t.write(blessing, align="center", font=("Arial", 16, "normal"))

def create_fireworks():
    """Create festive fireworks"""
    for _ in range(8):
        x = random.randint(-300, 300)
        y = random.randint(-100, 200)
        size = random.randint(20, 50)
        colors = ["#FFD700", "#FF6B35", "#E91E63", "#4CAF50", "#2196F3"]
        
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color(random.choice(colors))
        
        for _ in range(8):
            t.forward(size)
            t.backward(size)
            t.left(45)

# Draw the complete greeting card
draw_ornamental_border()

# Draw multiple diyas
for x in [-200, -100, 0, 100, 200]:
    draw_diya(x, -150, 40)

# Draw decorative flowers
flower_colors = ["#FF6B35", "#FFD700", "#E91E63", "#4CAF50"]
for i, x in enumerate([-250, -150, 150, 250]):
    draw_flower(x, 180, 20, flower_colors[i % len(flower_colors)])

write_text()
create_fireworks()

# Keep window open
turtle.mainloop()