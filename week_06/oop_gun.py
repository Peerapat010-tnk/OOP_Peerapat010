class Gun:
    def __init__(self,name,ammo,hp):
        self.ชื่อ = name
        self.กระสุน = ammo
        self.พลังชีวิต = hp
    def add_ammo(self,ammo):
        self.กระสุน += ammo
    def fire_ammo(self):
        if self.กระสุน > 0:
            self.กระสุน -= 1
        else:
            print("กระสุนหมด")
    def fire_gun(self,enemy):
        self.กระสุน -= 1
        enemy.พลังชีวิต -= 3
        
gun1 = Gun("t1",5,10)
gun2 = Gun("t2",10,10)
gun2.fire_gun(gun1)
print(gun2.กระสุน)
print(gun1.พลังชีวิต)
