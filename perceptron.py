class perceptron:
    # n is  number of weights
    # l is  learning Rate 
    # sizeOfPlane it use for make boundry size of plane 
    
    def __init__(self,n,l,sizeOfPlane):
        self.weights = []
        self.learning_Rate =l
        
        #set random weights
        for i in range(n):
            self.weights.append(random(0,1))
    
        print(self.weights)
        self.Size = sizeOfPlane
        # make a random  color 
        self.c = [random(255) ,random(255) ,random(255)]
    
    
    def plot(self):
        # input to plane
        # self.a = self.a -10 
        w0 = self.weights[0]
        w1 = self.weights[1]
        w2 = self.weights[2]
        w3 = self.weights[3]
        self.plane = Plane(w3,w2,w1,w0,self.Size,self.c)
        # self.plane.change(self.a,0);
        self.plane.draw()
    
    def guss(self,input):
        w0 = self.weights[0]
        w1 = self.weights[1]
        w2 = self.weights[2]
        w3 = self.weights[3]
        
        if(0< len(input)<=3):
            # give input as X,Y,Z 
            value = w3*input[0] + w2*input[1] + w1*input[2] +w0
            
            if(value>=1): return 1
            else: return -1
        # to error identification
        else: 
            return 0
        
    def train(self,error,inputs):
        
        for i in range(1,4):
            self.weights[3-i+1] += inputs[i-1]*self.learning_Rate*error
            
        self.weights[0] += self.learning_Rate*error
        print(self.weights,error,inputs)
        self.plot();
