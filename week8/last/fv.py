class Student:
    def __init__(self, name, grade, height):
        self.name = name
        self.grade = grade
        self.height = height
    def Info(self):
        print("이름:" + self.name + " 학년:" + self.grade + " 키:k  i " + self.height)



student1 = Student("곰", "5", "160")
student2 = Student("고양이", "5", "70")
student1.Info()
student2.Info()