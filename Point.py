# Kalana Dhanajaya Rathnayake 
# LifeF@github.com 
# University of Peradeniya 

# email : edata.incore@gmail.com

# 3D perceptron learning demonstration

class Point:
    # constructor prameters are x,y,z,c 
    # x y z is codenates of point and c is color
    def __init__(self , x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.error = True
    
    
    def getPoint(self):
        return [self.x,self.y,self.z]
    # point draw 
    def draw(self):
        # print("point draw")
        pushMatrix()
        stroke(20,200,20)
        fill(20,200,20)
        if(self.error):
            stroke(200,20,20)
            fill(200,20,20)
        
        translate(self.x,-self.y,self.z)
        sphere(1)
        noStroke()
        noFill()
        popMatrix()
        
    def updateState(self , ErrorState):
        self.error = ErrorState 
        self.draw()
    
