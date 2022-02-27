class Developer:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def getName(self):
        return self.name

    def getSalary(self):
        if self.year < 3:
            return 2800 + (self.year * 100)
        elif 3 <= self.year < 7:
            return 3500 + (self.year * 100)
        else:
            return 4500 + (self.year * 100)







d1 = Developer("박근원", 2)
d2 = Developer("김희진", 5)
d3 = Developer("박현준", 9)

print(d1.name + "의 연봉은 " + str(d1.getSalary()) + "만원입니다.")
print(d2.getName() + "의 연봉은 " + str(d2.getSalary()) + "만원입니다.")
print(d3.getName() + "의 연봉은 " + str(d3.getSalary()) + "만원입니다.")