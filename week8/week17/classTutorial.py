class Student:
    def __init__(self, name, grade, length):
        self.name = name
        self.grade = grade
        self.length = length


    def introduction(self):
        print("이름: " + self.name + " / 학년: " + self.grade + " / 키: " + self.length)




studentInfo1 = input("이름, 학년, 키를 입력하시오\n")
studentInfo2 = input("이름, 학년, 키를 입력하시오\n")
studentInfoList1 = studentInfo1.split(" ")
studentInfoList2 = studentInfo2.split(" ")
student1 = Student(studentInfoList1[0], studentInfoList1[1], studentInfoList1[2])
student2 = Student(studentInfoList2[0], studentInfoList2[1], studentInfoList2[2])
student1.introduction()
student2.introduction()