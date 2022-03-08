def dis(price, discount):
    ds = price*(discount/100)
    sp = price-ds
    return sp
ori_price = int(input("Enter Original Price : "))
dis_per = int(input("Enter Discount Percentage : "))
x=dis(ori_price, dis_per)
print(x)
##ori_price=120
##dis_per=5
##x=dis(120,5)
##def dis(120,5):
##    ds=120*(5/100)=6
##    sp=120-6=114
##x=114
