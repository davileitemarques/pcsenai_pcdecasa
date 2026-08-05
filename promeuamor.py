import turtle
tartaruga = turtle.Turtle()
tartaruga.pencolor("#001F3F")
def fazer_curva():
    for i in range(200):
        tartaruga.right(1)
        tartaruga.forward(1)
def desenhar_coracao():
    tartaruga.fillcolor("#001F3F")
    tartaruga.begin_fill()
    tartaruga.left(140)
    tartaruga.forward(113)
    fazer_curva()
    tartaruga.left(120)
    fazer_curva()
    tartaruga.forward(112)
    tartaruga.end_fill()
def inserir_texto():
    tartaruga.up()
    tartaruga.setpos(-53, 95)
    tartaruga.color('white')
    tartaruga.write("Eu te amo", font=( "Verdana", 14, "bold"))
    tartaruga.setpos(-58, 75)
    tartaruga.write("meu amor!!", font=("Verdana", 14, "bold"))


desenhar_coracao()
inserir_texto()

tartaruga.ht()
tartaruga.screen.mainloop()