class Hero:
    def __init__(self, name, hp, speed, dmg):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.dmg = dmg
        print(name + "(이/가) 생성 되었습니다.")

    def move(self):
        print(self.name + "(이/가) " + str(self.speed) + "의 속도로 이동했습니다.")

    def skill(self):
        print(self.name + "(이/가) 기술을 사용했습니다.")

    def getDetailInfo(self):
        return "이름: "+ self.name + "\n체력: " + str(self.hp) + "\n속도 :" + str(self.speed) + "\n공격력: " + str(self.dmg) + "\n"

    def attack(self, victim):
        print(self.name + "(이/가)" + victim.name + "(을/를) 공격해 " + str(self.dmg) + "만큼의 피해를 입혀 체력이 "
              + str(victim.hp) + "에서 " + str(victim.hp - self.dmg) + "으로 변경되었습니다.\n")
        victim.hp -= self.dmg

hanzo = Hero("hanzo", 200, 50, 120)
lucio = Hero("lucio", 200, 100, 40)

hanzo.move()
hanzo.skill()
print(hanzo.getDetailInfo())

lucio.move()
lucio.skill()
print(lucio.getDetailInfo())

hanzo.attack(lucio)
lucio.attack(hanzo)

print(hanzo.getDetailInfo())
print(lucio.getDetailInfo())