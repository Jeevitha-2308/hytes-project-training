class flower():
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def setcolor(self,color):
          self.color=color
    def getcolor(self):
        return self.name,self.num,self.color

if __name__=="__main__":
    x=flower("rose",1)
    x.setcolor("pink")
    print(x.getcolor())
  
