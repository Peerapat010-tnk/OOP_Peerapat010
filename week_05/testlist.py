money = []
while True:
    num = int(input("หยอดเงินใส่กระปุก"))
    money.append(num)
    print(money)
    if num == 0:
        print(f"เงินเก็บทั้งหมด = {sum(money)}")
        break
# money.append(20) คำสั่งเพิ่ม เพิ่มหลังสุด
# money.insert(1,50) คำสั่งแทรก อันแรกอินเด็ก อันสองค่าที่อยากจะใส่
# money.remove(50) คำสั่งลบ ต้องใส่ค่าที่จะลบ
# money.pop(1) คำสั่งลบ ต้องใส่อินเด็กที่จะลบ
# del money[1:2] คำสั่งลบตั้งแต่ตำแหน่งเท่าไหร่ถึงเท่าไหร่