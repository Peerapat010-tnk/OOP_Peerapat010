#โปรแกรมแกรมสูตรคูณแบบรับค่า คูณจาก 1 ไป 24 แสดงผลเฉพาะผลลัพธ์ที่หารด้วย 2 แล้วเป็นเลขคี่
num = int(input("ใส่ค่า"))
loop = 1
while loop <= 24:
    if num * loop / 2 % 2 != 0:
        print(f"{num} X {loop} = {num*loop}")
    loop += 1