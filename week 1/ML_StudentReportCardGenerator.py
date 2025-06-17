

def avg(marks):
    sum=0;
    for i in marks["Marks"]:
        sum+=i
    return sum/len(marks["Marks"])

def grader(avg):

        if(80<= avg<=100):
           return 'A'
        elif(60 <= avg <= 79):
           return 'B'
        elif(40 <= avg <=59):
           return 'C'
        else:
            return 'F'


def incmarks(marks):
    for i in range(len(marks["Subject"])):
        marks["Marks"][i]+=5
    return marks




name = input("Enter your name ")
age = input("Enter your age ")

marks={"Subject":["English","Math","Urdu"],"Marks":[]}

for i in range(len(marks["Subject"])):
    subject = marks["Subject"][i]
    marks["Marks"].append( int(input(f"Enter marks for {subject}: ")))

bonus = input("Add 5 bonus marks to all subjects? (yes/no)")
if(bonus == "yes"):
    print(incmarks(marks))

print(f"Name: {name}"
      f"\nAge: {age}")
for i in range(len(marks["Subject"])):
    subject = marks["Subject"][i]
    mark = marks["Marks"][i]

    print(f"{subject}: {mark}")


average = avg(marks)
print(round(average,2))
print(grader(average))