import random as woomee
class Student:
    def __init__(self,ชื่อ,ชื่อเล่น,คะแนนสอบ):
        self.name = ชื่อ
        self.nickname = ชื่อเล่น
        self.score = คะแนนสอบ
    def random(self):
        r = woomee.randint(1,10)
        self.score += r
    def grade(self):
        if self.score >= 5 :
            print("สอบผ่าน")
        else:
            print("สอบตก")
std1 = Student(ชื่อ="เจษฎาพร สุทธิวัฒนกำจร",ชื่อเล่น="เพ้น",คะแนนสอบ=0)
std2 = Student(ชื่อ="ภีรภัทร์ รักหวาน",ชื่อเล่น="กาตี้",คะแนนสอบ=0)
std3 = Student(ชื่อ="ภูนิวัช วงศ์ไพบูลย์กุล",ชื่อเล่น="อโตมิค",คะแนนสอบ=0)
std4 = Student(ชื่อ="ศรีสุเทพ หนูทอง",ชื่อเล่น="ออม",คะแนนสอบ=0)
std5 = Student(ชื่อ="สรพัศ ทองเผือก",ชื่อเล่น="ภูมิ",คะแนนสอบ=0)

std1.random()
std2.random()
std3.random()
std4.random()
std5.random()

print(std1.name,std1.nickname,std1.score)
std1.grade()
print(std2.name,std2.nickname,std2.score)
std2.grade()
print(std3.name,std3.nickname,std3.score)
std3.grade()
print(std4.name,std4.nickname,std4.score)
std4.grade()
print(std5.name,std5.nickname,std5.score)
std5.grade()