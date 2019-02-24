# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: Create a new turtle. We'll call it "bob"
jd = turtle.Turtle()

# Step 3: Move in the direction Bob's facing for 50 pixels
#bob.forward(50)
#bob.left(45)
#bob.forward(200)

def Carre(dist,angle):
    jd.left(angle)
    for i in range(0, 4):
        jd.fd(dist)
        jd.left(90)
    jd.left(-angle)

#Carre(100,45)
#Carre(150,0)



def etoile(a,b,angle):
    jd.left(angle)
    for i in range(0, 8):
        jd.fd(a)
        jd.right(45)
        jd.fd(b)
        jd.left(90)
        jd.fd(b)
        jd.right(45)
        jd.fd(a)
        jd.left(45)
    jd.left(-angle)

etoile(20,30,0)









# Step 4: We're done!
turtle.done()

