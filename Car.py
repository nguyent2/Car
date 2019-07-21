import turtle
wns = turtle.Screen()
def banh_xe(bichthuy):
    bichthuy.shape("circle")
    bichthuy.shapesize(0.1,0.1)
    bichthuy.speed(10)
    bichthuy.pensize(3)
    def ve_hinh_tron(number,cao):
        for i in range(number):
            bichthuy.right(1)
            bichthuy.forward(cao)
    ve_hinh_tron(360, 0.5)
    def ve_tron(solieu, chieucao):
        for i in range(solieu):
            bichthuy.left(1)
            bichthuy.backward(chieucao)
    ve_tron(90, 0.5)
    bichthuy.left(90)
    bichthuy.forward(40)
    bichthuy.right(90)
    ve_hinh_tron(180,2.5)
    bichthuy.right(90)
    bichthuy.forward(40)
    bichthuy.left(90)
    ve_hinh_tron(360, 0.5)
    ve_tron(180, 0.5)
    bichthuy.left(90)
    bichthuy.forward(95)

wns.bgcolor("#ffffff")

thy = turtle.Turtle()
thy.color("#ccffff")
thy.begin_fill()
banh_xe(thy)
thy.end_fill()

def annyong(mauu):
    ngoc = turtle.Turtle()
    ngoc.color("#e6ffff")
    ngoc.penup()
    ngoc.forward(mauu)
    ngoc.pendown()
    ngoc.begin_fill()
    banh_xe(ngoc)
    ngoc.end_fill()

annyong(50)
annyong(100)
annyong(150)
annyong(200)

thuy = turtle.Turtle()
thuy.color("#ccffff")
thuy.penup()
thuy.forward(250)
thuy.pendown()
thuy.begin_fill()
banh_xe(thuy)
thuy.end_fill()


wns.exitonclick()
