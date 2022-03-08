class bloodbank():
    def _init_(self,name,age,bloodtype):
        self.name=name
        self.age=age
        self.bloodtype=bloodtype
        print(self.bloodtype)
    def apositive(self,bloodcollection):
        print("name -->",self.name)
        print("age -->",self.age)
        print("bloodtype -->",self.bloodtype)
        count=bloodcollection[self.bloodtype]
        print("remaining blood available ",count-1)
    
    def bpositive(self,bloodcollection):
        print("name -->",self.name)
        print("age -->",self.age)
        print("bloodtype -->",self.bloodtype)
        count=bloodcollection[self.bloodtype]
        print("remaining blood available ",count-1)        
    def abpositive(self):
        print("name -->",self.name)
        print("age -->",self.age)
        print("bloodtype -->",self.bloodtype)
        count=bloodcollection[self.bloodtype]
        print("remaining blood available ",count-1)

bloodcollection={"apositive":2,"bpositive":1,"abpositive":3}

bloodtype=input("enter the blood type :")
name=input("enter the name :")
age=int(input("enter the age: "))

bloodtype=bloodtype.strip()
if(bloodtype in bloodcollection):
    tt=bloodbank(name,age,bloodtype)
    if(bloodtype == "apositive"):
        tt.apositive(bloodcollection)
    elif(bloodtype == "bpositive"):
        tt.bpositive(bloodcollection)
