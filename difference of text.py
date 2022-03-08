a=open('program1.txt','r')
b=open('program2.txt','r')
con=a.readlines()
con1=b.readlines()
count=0
if(len(con)==len(con1)):
    for i in range(len(con)):
            if(con[i]!=con1[i]):
                count+=1
                print("line",count ,"is mismatch")
