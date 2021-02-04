import turtle
import math

tina = turtle.Turtle()
tina.shape("turtle")

r = 200
draw_inscribed_circle = False
tina.pensize(4)

dis = tina.getscreen().textinput(
    "Cirkel", "Zal ik eerst een cirkel tekenen?")
if dis == 'ja':
    draw_inscribed_circle = True

n = int(tina.getscreen().numinput(
    "Hoeken?", "Hoeveel hoeken zal ik tekenen?", 3, minval=3, maxval=100))

a = 180.0/n
d = 2 * r * math.tan(math.radians(a))

# draw inscribed circle
if draw_inscribed_circle:
    tina.penup()
    tina.goto(0,-r)
    tina.pendown()
    tina.circle(r)
    tina.penup()
    tina.home()
    tina.pendown()

tina.penup()
tina.goto(-d/2, r)
tina.pendown()

# draw ngon
for i in range(n):
    tina.forward(d)
    tina.right(2*a)

tina.write(f"Ik heb een figuur met {n} hoeken getekend!", font=('Arial', 16, 'normal'))

tina.getscreen().mainloop()