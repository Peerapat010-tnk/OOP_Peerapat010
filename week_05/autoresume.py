resume = {"name":str,"no":int,"hobby":str,"color":str}
num = int(input("จำนวนคนที่จะป้อน"))
for loop in range(1,num+1):
    print(f"กรุณากรอกคนที่{loop}")
    name = str(input("กรุณากรอกชื่อเล่น : "))
    resume["name"] = name
    no = int(input("กรุณากรอกเลขที่ : "))
    resume["no"] = no
    hobby = str(input("กรุณากรอกงานอดิเรก : "))
    resume["hobby"] = hobby
    color = str(input("กรุณากรอกสีที่ชอบ : "))
    resume["color"] = color
    print(f"ข้อมูลคนที่ {loop+1}\n",resume)