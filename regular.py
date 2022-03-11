import re
a=open("hytes.txt",'r')
b=a.read()
d="akki is very good girl supri"
c=re.sub("akki","jeevi",b)
print(c)
##
##import re
##
##list = ["guru99 get", "guru99 give", "guru Selenium"]
##for element in list:
##    z = re.match("(g\w+\Wg\w+)",element,re.M|re.I|re.U|re.S|re.X)
##    if(z!=None):
##        print(z.groups())
##
##
##xx = "guru99,education is fun"
##r1 = re.findall(r"\w+$", xx)
##print(r1)
##print (re.split(r'\d',b))


##import re
##xx = """guru99 
##careerguru99	
##Selenium."""
##k1 = re.findall(r"S\w+", xx)
##k2 = re.findall(r"S\w+", xx, re.M|re.S)
##print(k1)
##print(k2)
