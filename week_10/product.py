class Product:
    def __init__(self,name,stock):
        self.name = name
        self.__price = []
        self.__stock = stock
    def perm(self):
            self.__stock += product
    def lod(self):
            self.__stock -= product
    def edit(self):
        permprice = int(input("กรอกราคาสินค้า"))
        self.__price.append(permprice)
    def check(self):
        return (f"(จำนวน {self.__stock } ชิ้น ราคา{self.__price} บาท)")
        
peem1 = Product("bread",0)
while True:
    choice = input("กรุณาเลือกฟังก์ชัน ถ้าต้องการเพิ่มจำนวนสินค้าพิมพ์คำว่า perm ถ้าต้องลดจำนวนสินค้าพิมพ์คำว่า lod ถ้าอยากเช็คสินค้าพิมพ์คำว่า check ออกพิมพ์คำว่า exit : ")
    if choice == "perm":
        product = int(input("ใส่จำนวนที่ต้องการเพิ่ม : "))
        peem1.perm()
    elif choice == "lod":
        product = int(input("ใส่จำนวนที่ต้องการลด : "))
        peem1.lod()
    elif choice == "edit":
        peem1.edit()
    elif choice == "check":
        print(f"ชื่อสินค้า {peem1.name} มีรายละเอียดดังนี้ {peem1.check()}")
    elif choice == "exit":
        break