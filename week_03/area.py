print("คำนวณหาพื้นที่ 4 เหลี่ยมจัตุรัส")
size = int(input("ใส่ความยาวด้าน : ")) 
sum = size **2
print("พื้นที่ 4 เหลี่ยมจัตุรัสนี้ คือ " ,(sum))

print("คำนวณพื้นที่ 4 เหลี่ยมผืนผ้า")
wide = int(input("ใส่ความกว้าง :"))
long = int(input("ใส่ความยาว :"))
sum1 = wide * long
print("พื้นที่ 4 เหลี่ยมผืนผ้านี้ คือ " ,(sum1))

print("คำนวณพื้นที่วงกลม")
radius = float(input("ใส่ความยาวรัศมี :"))
pire = 3.14
sum2 = radius * radius * pire
print("พื้นที่วงกลม คือ " ,(sum2))