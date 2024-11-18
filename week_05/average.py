value = []
num = int(input("ต้องการป้อนค่าทั้งหมดกี่ตัว"))
for loop in range(1,num+1):
    num = int(input(f"ใส่ตัวที่{loop} : "))
    value.append(num)
print(f"ค่าเฉลี่ยของ {value} = {sum(value)/len(value)}")