# Kalana Dhanajaya Rathnayake 
# LifeF@github.com 
# University of Peradeniya 

# email : edata.incore@gmail.com

# 3D perceptron learning demonstration

class Plane:
    coef = []
    def __init__(self,w3,w2,w1,w0,planeSize ,colour):
        self.coef = []
        self.coef.append(w0)
        self.coef.append(w1) 
        self.coef.append(w2)
        self.coef.append(w3)
        self.colour = color(20,20,0)
        if (0<= len(colour)<=3):
            self.colour = color(colour[0],colour[1],colour[2])
        else:
            print("colour is not set")
        self.PlaneSize = planeSize
        
    def changeWhole(self,coef):
        if(len(coef)==4):
            self.coef[3] = coef[3]
            self.coef[2] = coef[2]
            self.coef[1] = coef[1]
            self.coef[0] = coef[0]
            self.draw()
            return True 
        else :
            return False 
    
    def change(self, update_value , coef ):
        if(coef>=0 & coef<4):
            self.coef[coef] = update_value 
            self.draw()
            return True 
        else:
            return False 
    
    
    def draw(self):
        fill(self.colour,63);
        beginShape();
    
        # need find z intercept to draw to plane 
        # find corresponding z value at (PlaneSize,PlaneSize),(PlaneSize,-PlaneSize),(-PlaneSize,PlaneSize) and (-PlaneSize,-PlaneSize)
        # (PlaneSize,PlaneSize)   z value take as z1
        # (PlaneSize,-PlaneSize)  z value take as z2
        # (-PlaneSize,PlaneSize)  z value take as z3
        # (-PlaneSize,-PlaneSize) z value take as z4
        
        # take Plane size 
        S = self.PlaneSize
        # take weights and w0 is bias 
        w0 = self.coef[0] # bias
        w1 = self.coef[1] # z weight
        w2 = self.coef[2] # y weight
        w3 = self.coef[3] # x weight
        
        # calculate z value
        z1 = -(w3*(S)  + w2*(S)  + w0)/w1
        z2 = -(w3*(S)  + w2*(-S) + w0)/w1
        z3 = -(w3*(-S) + w2*(S)  + w0)/w1
        z4 = -(w3*(-S) + w2*(-S) + w0)/w1
        
        vertex( S,-S,z1)
        vertex(-S,-S,z3)
        vertex(-S,S,z4)
        vertex( S,S,z2)
    
        endShape(CLOSE);
    
    def guss(self,input):
        
        w0 = self.coef[0] # bias
        w1 = self.coef[1] # z weight
        w2 = self.coef[2] # y weight
        w3 = self.coef[3] # x weight
        
        if(0< len(input)<=3):
            # give input as X,Y,Z 
            value = w3*input[0] + w2*input[1] + w1*input[2] +w0
            
            if(value>=1): return 1
            else: return -1
        # to error identification
        else: 
            return 0
        
