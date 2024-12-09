class Student:
    def __init__(self,std_name,std_id,std_age,std_grades,):
        self.name = std_name
        self.id = std_id
        self.age = std_age
        self.grades = std_grades
         
    def modify(self):
        self.grades["Match"] = float(input("ใส่เกรดคณิต : "))
        self.grades["Thai"] = float(input("ใส่เกรดไทย : "))
        self.grades["Eng"] = float(input("ใส่เกรดอังกิด : "))
        self.grades["sci"] = float(input("ใส่เกรดวิทย์ : "))
        self.grades["social"] = float(input("ใส่เกรดสังคม : "))
        
    def avg_grades(self):
        return {sum(self.grades.values())/len(self.grades)}
        
std1 = Student("อ้ายวูมี่",67319010010,18,{})
std1.modify()
average = std1.avg_grades()
print(f"{std1.name} ได้เกรดเฉลี่ย {average}")
print(std1.name,std1.id,std1.age,std1.grades)