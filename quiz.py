import pgzrun

WIDTH = 800
HEIGHT = 500
TITLE = "quiz master"

# Rect(x,y,WIDTH,HEIGHT)
marquee_box = Rect(20,0,WIDTH,70)

question_box = Rect(0,80,625,100)

timer_box = Rect(650,80,150,100)

answer_box1 = Rect(0,200,300,125)
answer_box2 = Rect(0,350,300,125)
answer_box3 = Rect(325,200,300,125)
answer_box4 = Rect(325,350,300,125)

skip_box = Rect(650,200,150,400)

message = "welcome to quiz master"

def draw():
    # drawring rectangles
    screen.fill("pink")
    screen.draw.filled_rect(marquee_box,"orange")
    screen.draw.filled_rect(question_box,"white")
    screen.draw.filled_rect(timer_box,"green")
    screen.draw.filled_rect(answer_box1,"orange")
    screen.draw.filled_rect(answer_box2,"orange")
    screen.draw.filled_rect(answer_box3,"orange")
    screen.draw.filled_rect(answer_box4,"orange")
    screen.draw.filled_rect(skip_box,"black")
# writing 
    screen.draw.textbox(message,marquee_box,color = "black")

def update():
    marquee_box.x+=-1

pgzrun.go()