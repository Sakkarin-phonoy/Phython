# ค้นหาตัวเลข มากสุด / น้อยสุด
max ,min = 0,999999
while True :
    number=int(input("ป้อนตัวเลข :")) 
    if number<0 :
        break
    if number>max :
        max=number
    if number<min:
        min=number

print("ค่าสูงสุด = ", max)
print("ค่าต่ำสุด = ",min)