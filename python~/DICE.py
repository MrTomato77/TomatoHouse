import random

class Dice:                                           # ประกาศ class Dice                               
    __face = 0                                        # เก็บค่าของหน้าที่ออก (encapsulation)
    def roll(self):
        self.__face = random.randint(1, 6)            # นำค่า __face มาสุ่มคั้งแต่ค่า 1-6
    def face(self):
        return self.__face                            # เรียกใช้ค่า __face

class PyramidDice(Dice):                              # ประกาศ subClass PyramidDice โดยมี parent เป็น class Dice
    def roll(self):
        self.__face = random.randint(1, 4)            # นำค่า __face ของ parent class มาสุ่มคั้งแต่ค่า 1-4
    def face(self):
        return self.__face                            # เรียกใช้ค่า __face

class DiceBox:
    def __init__(self):
        self.dices = []                                # สร้าง empty list ไว้เก็บค่าของหน้าที่ออก
    def add(self, dice):
        self.dices.append(dice)                        # เพิ่มค่าที่ออกไปใน list dices
    def shake(self):
        for dice in self.dices:
            dice.roll()                                # สลับคำแหน่งภายใน list
    def get_faces(self):
        self.lst = [dice.face() for dice in self.dices]         # สร้าง list ของหน้าที่ออกของ Dice ทั้งหมด
        self.sigma = sum(self.lst)                              # รวมค่าของ Dice ทั้งหมด
        return f'{self.lst} = {self.sigma}'

box = DiceBox()
box.add(Dice())
box.add(Dice())
box.add(PyramidDice())
for i in range(10):
    box.shake()
    print(box.get_faces())