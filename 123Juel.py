#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif"
 # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50

#list thingy
screen_width = 400
screen_height = 400
letter_list = ["a","b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

current_letters = []
apple_list = []
number_of_apples = 5

current_letter = "a"


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
 # Make the screen aware of the new file


wn.bgpic("background.gif")
'''
apple = trtl.Turtle()
apple.penup()
'''
wn.tracer(False)



# given a turtle, set that turtle to be shaped by the image file
def reset_apple(active_apple):
  global current_letter
  length_of_list = len(letter_list)
  if (length_of_list != 0):
    index = rand.randint(0, length_of_list)
    current_letter = letter_list.pop(index)
    active_apple.goto(rand.randint((-screen_width)/2, (screen_width)/2), rand.randint(-(screen_height)/2, (screen_height)/2))
    draw_apple(active_apple, current_letter)
    current_letters.append(current_letter)


def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  draw_letter(letter, active_apple)
  active_apple.showturtle()
  wn.update()
  

def apple_fall(letter):
  wn.tracer(True)
  index = current_letters.index(letter)
  current_letters.pop(index)

  active_apple = apple_list.pop(index)

  active_apple.goto(active_apple.xcor(), ground_height)
  active_apple.clear()
  active_apple.hideturtle()
  wn.tracer(False)
  reset_apple(active_apple)
  apple_list.append(active_apple)


def draw_letter(letter, active_apple):
  active_apple.color("black")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("MS Sans Serif", 74, "bold"))
  active_apple.setpos(remember_position)

for i in range(number_of_apples):
  active_apple = trtl.Turtle(shape = apple_image)
  active_apple.penup()
  reset_apple(active_apple)
  apple_list.append(active_apple)

def check_letter_a():
  if ("a" in current_letters):
    apple_fall("a")

def check_letter_b():
  if ("b" in current_letters):
    apple_fall("b")

def check_letter_c():
  if ("c" in current_letters):
    apple_fall("c")

def check_letter_d():
  if("d" in current_letters):
    apple_fall("d")

def check_letter_e():
  if("e" in current_letters):
    apple_fall("e")

def check_letter_f():
  if ("f" in current_letters):
    apple_fall("f")

def check_letter_g():
  if("g" in current_letters):
    apple_fall("g")

def check_letter_h():
  if("h" in current_letters):
    apple_fall("h")

def check_letter_i():
  if ("i" in current_letters):
    apple_fall("i")

def check_letter_j():
  if ("j" in current_letters):
    apple_fall("j")

def check_letter_k():
  if("k" in current_letters):
    apple_fall("k")

def check_letter_l():
  if("l" in current_letters):
    apple_fall("l")

def check_letter_m():
  if ("m" in current_letters):
    apple_fall("m")

def check_letter_n():
  if("n" in current_letters):
    apple_fall("n")

def check_letter_o():
  if ("o" in current_letters):
    apple_fall("o")

def check_letter_p():
  if ("p" in current_letters):
    apple_fall("p")

def check_letter_q():
  if ("q" in current_letters):
    apple_fall("q")

def check_letter_r():
  if ("r" in current_letters):
    apple_fall("r")

def check_letter_s():
  if("s" in current_letters):
    apple_fall("s")

def check_letter_t():
  if ("t" in current_letters):
    apple_fall("t")

def check_letter_u():
  if ("u" in current_letters):
    apple_fall("u")

def check_letter_v():
  if("v" in current_letters):
    apple_fall("v")

def check_letter_w():
  if ("w" in current_letters):
    apple_fall("w")

def check_letter_x():
  if ("x" in current_letters):
    apple_fall("x")

def check_letter_y():
  if ("y" in current_letters):
    apple_fall("y")

def check_letter_z():
  if ("z" in current_letters):
    apple_fall("z")

draw_apple(active_apple, "a")


wn.onkeypress(check_letter_a, "a")
wn.onkeypress(check_letter_b, "b")
wn.onkeypress(check_letter_c, "c")
wn.onkeypress(check_letter_d, "d")
wn.onkeypress(check_letter_e, "e")
wn.onkeypress(check_letter_f, "f")
wn.onkeypress(check_letter_g, "g")
wn.onkeypress(check_letter_h, "h")
wn.onkeypress(check_letter_i, "i")
wn.onkeypress(check_letter_j, "j")
wn.onkeypress(check_letter_k, "k")
wn.onkeypress(check_letter_l, "l")
wn.onkeypress(check_letter_m, "m")
wn.onkeypress(check_letter_n, "n")
wn.onkeypress(check_letter_o, "o")
wn.onkeypress(check_letter_p, "p")
wn.onkeypress(check_letter_q, "q")
wn.onkeypress(check_letter_r, "r")
wn.onkeypress(check_letter_s, "s")
wn.onkeypress(check_letter_t, "t")
wn.onkeypress(check_letter_u, "u")
wn.onkeypress(check_letter_v, "v")
wn.onkeypress(check_letter_w, "w")
wn.onkeypress(check_letter_x, "x")
wn.onkeypress(check_letter_y, "y")
wn.onkeypress(check_letter_z, "z")


wn.listen()
trtl.mainloop()