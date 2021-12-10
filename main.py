#-----import statements-----
import turtle as trtl
import random as rand

wn = trtl.Screen()

#-----the letters-----
lettert = trtl.Turtle()
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#-----setting up the letters-----
lettert.color("white")
font_setup = "merry", 100, "normal"
lettert.penup()
lettert.goto(-20,-75)
lettert.pendown()
for i in range(1):
  letter = rand.choice(letters)
  lettert.write((letter), font=font_setup)
lettert.hideturtle()

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

score = -1

#-----countdown writer-----
counter =  trtl.Turtle()
counter.color("white")
counter.penup()
counter.goto(100,100)
counter.pendown()
counter.hideturtle()

#-----score writer-----
score_writer = trtl.Turtle()
score_writer.color("white")
score_writer.penup()
score_writer.goto(-200,100)
score_writer.hideturtle()

#-----asking for name and giving instructions-----
end = trtl.Turtle()
end.color("yellow")
end.penup()
end.goto(-75,-100)
end.hideturtle()

#-----game functions-----
def write_letter():
  global letter
  letter = rand.choice(letters)
  font_setup = "merry", 100, "normal"
  lettert.write((letter), font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer >= 0 and timer <= 5:
    counter.color("red")
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    name = input("what is your name?")
    end.write("Good Job, " +name+ "!", font=font_setup)
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
  
def goawayletter():
  lettert.clear()

def score_update():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

def spot_clicked():
  global timer_up
  if (not timer_up):
    score_update()
    write_letter()
  else:
    lettert.hideturtle

#-----functions for typed letter-----
def typedA():
  if letter == "A":
    goawayletter()
    spot_clicked()

def typedB():
  if letter == "B":
    goawayletter()
    spot_clicked()

def typedC():
  if letter == "C":
    goawayletter()
    spot_clicked()

def typedD():
  if letter == "D":
    goawayletter()
    spot_clicked()

def typedE():
  if letter == "E":
    goawayletter()
    spot_clicked()

def typedF():
  if letter == "F":
    goawayletter()
    spot_clicked()

def typedG():
  if letter == "G":
    goawayletter()
    spot_clicked()

def typedH():
  if letter == "H":
    goawayletter()
    spot_clicked()

def typedI():
  if letter == "I":
    goawayletter()
    spot_clicked()

def typedJ():
  if letter == "J":
    goawayletter()
    spot_clicked()

def typedK():
  if letter == "K":
    goawayletter()
    spot_clicked()

def typedL():
  if letter == "L":
    goawayletter()
    spot_clicked()

def typedM():
  if letter == "M":
    goawayletter()
    spot_clicked()

def typedN():
  if letter == "N":
    goawayletter()
    spot_clicked()

def typedO():
  if letter == "O":
    goawayletter()
    spot_clicked()

def typedP():
  if letter == "P":
    goawayletter()
    spot_clicked()

def typedQ():
  if letter == "Q":
    goawayletter()
    spot_clicked()

def typedR():
  if letter == "R":
    goawayletter()
    spot_clicked()

def typedS():
  if letter == "S":
    goawayletter()
    spot_clicked()

def typedT():
  if letter == "T":
    goawayletter()
    spot_clicked()

def typedU():
  if letter == "U":
    goawayletter()
    spot_clicked()

def typedV():
  if letter == "V":
    goawayletter()
    spot_clicked()

def typedW():
  if letter == "W":
    goawayletter()
    spot_clicked()

def typedX():
  if letter == "X":
    goawayletter()
    spot_clicked()

def typedY():
  if letter == "Y":
    goawayletter()
    spot_clicked()

def typedZ():
  if letter == "Z":
    goawayletter()
    spot_clicked()

#-----key press and essentials-----
countdown()
score_update()
wn.onkeypress(typedA, "a")
wn.onkeypress(typedB, "b")
wn.onkeypress(typedC, "c")
wn.onkeypress(typedD, "d")
wn.onkeypress(typedE, "e")
wn.onkeypress(typedF, "f")
wn.onkeypress(typedG, "g")
wn.onkeypress(typedH, "h")
wn.onkeypress(typedI, "i")
wn.onkeypress(typedJ, "j")
wn.onkeypress(typedK, "k")
wn.onkeypress(typedL, "l")
wn.onkeypress(typedM, "m")
wn.onkeypress(typedN, "n")
wn.onkeypress(typedO, "o")
wn.onkeypress(typedP, "p")
wn.onkeypress(typedQ, "q")
wn.onkeypress(typedR, "r")
wn.onkeypress(typedS, "s")
wn.onkeypress(typedT, "t")
wn.onkeypress(typedU, "u")
wn.onkeypress(typedV, "v")
wn.onkeypress(typedW, "w")
wn.onkeypress(typedX, "x")
wn.onkeypress(typedY, "y")
wn.onkeypress(typedZ, "z")
wn.listen()
wn.bgpic("backg.gif")
wn.mainloop()