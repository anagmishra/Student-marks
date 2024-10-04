class Student:
    def __init__(self, name, clas, section):
        self.name = name
        self.clas = clas
        self.section = section

    def desc(self):
        print(f"The student name is {self.name} who is in {self.clas}{self.section}.")

class ReportCard(Student):
    def __init__(self, name, clas, section, subject, marks):
        super().__init__(name, clas, section)
        self.subject = subject
        self.marks = marks
    
    def output(self):
        if self.marks>=90 and self.marks<=100:
            print(f"The student name is {self.name} who is in {self.clas}{self.section} and has A+ grades in {self.subject}")
        elif self.marks>=85 and self.marks<=89:
            print(f"The student name is {self.name} who is in {self.clas}{self.section} and has A grades in {self.subject}")
        elif self.marks>=80 and self.marks<=84:
            print(f"The student name is {self.name} who is in {self.clas}{self.section} and has B+ grades in {self.subject}")
        elif self.marks>=75 and self.marks<=79:
            print(f"The student name is {self.name} who is in {self.clas}{self.section} and has B grades in {self.subject}")
        elif self.marks>=70 and self.marks<=74:
            print(f"The student name is {self.name} who is in {self.clas}{self.section} and has C+ grades in {self.subject}")
        elif self.marks>=65 and self.marks<=69:
            print(f"The student name is {self.name} who is in {self.clas}{self.section} and has C grades in {self.subject}")
        elif self.marks>=60 and self.marks<=64:
            print(f"The student name is {self.name} who is in {self.clas}{self.section} and has D+ grades in {self.subject}")
        elif self.marks>=50 and self.marks<=59:
            print(f"The student name is {self.name} who is in {self.clas}{self.section} and has D grades in {self.subject}")
        else:
            print(f"The student name is {self.name} who is in {self.clas}{self.section} and has F grades in {self.subject}")

Student1=ReportCard("Anag", 10, "G", "Maths", 98)
Student1.desc()
Student1.output()