#   a123_apple_1.py
import turtle as trtl


apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_letter("a", active_apple)
  wn.update()
  
def fall():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)

def draw_letter(letter, active_apple):
  active_apple.color("black")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("MS Sans Serif", 74, "bold"))
  active_apple.setpos(remember_position)

draw_apple(apple)
wn.onkeypress(fall, "a")

wn.listen()
trtl.mainloop()