import simplegui
import random 

y=-100
y2 = 0

COLOR = ["White", "Green", "Blue", "Yellow", "Orange", "Red"]

def draw_handler(canvas):
    #first color
    color = random.choice(COLOR)
    thickness = random.randint(1, 50)
    x = random.randint(100, 500)
    radius = random.randint(1, 100)
    #second color
    color2 = random.choice(COLOR)
    thickness2 = random.randint(1, 50)
    x2 = random.randint(100, 500)
    radius2 = random.randint(1, 100)
    global y
    global y2
    y = y + 5
    y2 = y2 - 5
    if (y > 700):
        y = 0
    if (y2 < 0):
        y2 = 700
        
        
        
    canvas.draw_circle((y,x), radius, thickness, color)
    canvas.draw_line((y, x), (y2, x2), thickness, color)
    canvas.draw_circle((y2,x2), radius2, thickness2, color2)
    canvas.draw_circle((x,y), radius, thickness, color)
    canvas.draw_line((x, y), (x2, y2), thickness, color)
    canvas.draw_circle((x2,y2), radius2, thickness2, color2)
    
    


frame = simplegui.create_frame('Colors', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
