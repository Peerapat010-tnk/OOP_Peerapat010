class Cat:
    def __init__(self,cat_name,cat_color):
        self.name = cat_name
        self.color = cat_color
    def cry(self):
        return self.name , "meow"
    def cry2(self):
        print(f"แมว{self.color} ชื่อ{self.cry()}")
mycat1 = Cat("ศรีสุเทพ","สีเขียว")
mycat2 = Cat("อ้ายวูมี่","สีแดง")
mycat1.cry2()
print(mycat1.name)
print(mycat2.color)