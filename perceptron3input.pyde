# Kalana Dhanajaya Rathnayake 
# LifeF@github.com 
# University of Peradeniya 

# email : edata.incore@gmail.com

# 3D perceptron learning demonstration 

# import point class 
from Point import Point  
from Plane import Plane 
from perceptron import perceptron 

# CONTROL VARIABLE
#----------------------------
# number of point 
NP = 200
# Learning Rate
LR = 0.000001
#-----------------------------
# Use for make rotate animation
Rotate = 0.0
# object creation
# real plane for clasify the value 
Actual_Plane = Plane(20,20,20,0,150,[0,20,20])
# crate Preceptron
percep = perceptron(4,LR,150)


Actual_Plane_locker =True
Points = []

def setup():
    size(800,800,P3D)
    global img
    for i in range(NP):
        x = int(random(-200,200))
        y = int(random(-200,200))
        z = int(random(-200,200))
        Points.append(Point(x,y,z))
    # background()
    img = loadImage("logo.png")
    frameRate(20)

def draw():
    global Rotate ,p1, pl1,percep,Points
    background(51)
    imageMode(CENTER)
    image(img, 40, height -40 ,50,50)
    fill(200)
    textAlign(LEFT)
    text("Rathnayake , R.M.K.D (LifeF@github)",75, height -48)
    text("University of Peradeniya",75, height -36)
    text("Department Of Computer Engineering (DLNN TEAM)",75, height -24)
    textAlign(CENTER)
    text("Perceptron Learning 3D Demostration",width/2 , 16)
    noFill()
    
    # tanslate 2D to 3D plane 
    translate(400,400,0)
    pushMatrix()
    #----------------------------
    stroke(100)
    rectMode(CENTER)
    
    # Rotate 
    #-------
    # Rotate PI/6 Over X axis 
    rotateX(PI/6)
    # Rotate Animation
    Rotate = Rotate + 0.01
    rotateZ(Rotate)
    #--------
    
    # make taransparant base plane 
    fill(20,20,0,11);
    rect(0,0,400,400);
    
    # Base line draw X,Y,Z
    drawBaseLine()
    for point in Points:
        a= point.getPoint();
        acg = Actual_Plane.guss(a)
        pcg = percep.guss(a)
        # error is actual guss - perceptron guss
        error = acg - pcg
        # adjust perceptron parameters when have ERROR
        if(error!=0): percep.train(error , a)
        
        if(acg != pcg):
            point.updateState(True)
        else : point.updateState(False)
        # point.draw()
    # perceptron action
     # p1.draw()
     # percep.plot()
    Actual_Plane.draw()

    
    # print(pl1.guss([-100,-100,200]))
    
    noFill()
    #------------------------------
    popMatrix()
    
    # add to make transparancy
    hint(DISABLE_DEPTH_TEST);


# function for create base line 
def drawBaseLine():
    line(0,-200,0,0,200,0)
    line(0,0,-200,0,0,200)
    line(200,0,0,-200,0,0)
