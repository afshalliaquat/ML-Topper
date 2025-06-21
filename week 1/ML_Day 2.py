import os.path

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_grade(subject,marks):
        grades["Subject"].append(subject)
        grades["Marks"].append(marks)


    def avg(marks):
        sum=0;
        for i in marks["Marks"]:
            sum+=i
        return sum/len(marks["Marks"])

    def grader(self,avg):

            if(80<= self.avg<=100):
               return 'A'
            elif(60 <= self.avg <= 79):
               return 'B'
            elif(40 <= self.avg <=59):
               return 'C'
            else:
                return 'F'

    def generate_report(self,grades):
        average = self.avg(grades)

        return f"Name: {name} \nAge: {age}\n{grades}\nAverage: {round(average, 2)} \nGrade: {grader(average)}"

    def incmarks(grades):
        for i in range(len(grades["Subject"])):
             grades["Marks"][i] =int(grades["Marks"][i]) + 5
        return grades

    def save_to_file(self,File,grades):
        with open(File,"a") as file:
           file.write(self.generate_report(grades))
        print("added")

    @staticmethod
    def load_from_file(File):
      if os.path.exists(File):
        with open(File,"r") as file:
            print(file.read())


name = input("Enter your name ")
age = input("Enter your age ")
student = Student(name,age)

grades={"Subject":[],"Marks":[]}

student.add_grade("Urdu",input("enter marks for Urdu"))
student.add_grade("English",input("enter marks for English"))
student.add_grade("Math",input("enter marks for Math"))
student.add_grade("Science",input("enter marks for Science"))



bonus = input("Add 100 bonus marks to all subjects? (yes/no)")
if(bonus == "yes"):
    print(student.incmarks(grades))

student.save_to_file("MLDAY2.txt",grades)
student.load_from_file("MLDAY2.txt")