class average():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
if __name__=="__main__":
    x=average(3,5)
    y=x.sum(3)
    z=x.sub()
    print(y)
    print(z)
    

        
