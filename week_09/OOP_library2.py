class Library:
    def __init__(self):
        self.bookname = []
        self.name = []
        self.page = []
        self.price = []
    def add_book(self):
        while True:
            choice = input("พิมพ์ add เพื่อเพิ่ม พิมพ์ exit เพื่อออก  :")
            if choice == 'add':
                     namebook = str(input('ใส่ชื่อหนังสือ : '))
                     self.bookname.append(namebook)
                     name = str(input('ใส่ชื่อผู้แต่ง : '))
                     self.name.append(name)
                     page = int(input('ใส่จำนวนหน้า : '))
                     self.page.append(page)
                     price = int(input('ใส่ราคา : '))
                     self.price.append(price)
            elif choice == 'exit':
                 break
    def show_books(self):
        print("รายชื่อหนังสือในห้องสมุด:")
        for show_book in self.bookname:
            print(show_book)
    def find_book(self):
        bookname = str(input('ค้นหาชื่อ:'))
        i = 0
        for i in self.bookname:
            if bookname == i:
                print(i)
lib1 = Library()
lib1.add_book()
lib1.show_books()
lib1.find_book()
print(f"ชื่อหนังสือ : {lib1.bookname} , ชื่อผู้แต่ง : {lib1.name} , จำนวนหน้า : {lib1.page} , ราคา : {lib1.price}")