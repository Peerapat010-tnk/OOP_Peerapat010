class Cat:
    def __init__(self,ชื่อ,อายุ,เพศ,สี):
        self.name = ชื่อ
        self.age = อายุ
        self.gender = เพศ
        self.color = สี
    def old(self):
        self.age += 1
cat1 = Cat(ชื่อ="ออม",อายุ="19",เพศ="ตัวผู้",สี="สีแดง")
cat2 = Cat("ศรีเงิน",5,"ตัวเมีย","สีขาว")
cat2.old()
print(cat2.age)