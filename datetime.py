from datetime import datetime
now = datetime.now()
t = now.strftime("%B:%m:%d")
print("Date:", t)
t1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date:", t1)
t2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("s2:", t2)
