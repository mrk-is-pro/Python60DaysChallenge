student=[]
name="ruthvik"
x=input("Enter the Name of the person entering Marks:")
if x==name.lower():
    v="?"
else:
    v=""
n=int(input("Enter No.of Students:"))
for i in range(n):
    student+=[int(input(f"Enter Marks of Student-{i+1}:"))]
vc=0
fc=0
for i in range(n):
    if student[i]>=90:
        vc+=1
        print(f"Student-{i+1} Marks={student[i]} --> Excellent" + v)
    elif student[i]>=75:
        vc+=1
        print(f"Student-{i+1} Marks={student[i]} --> Very Good"+ v)
    elif student[i]>=60:
        vc+=1
        print(f"Student-{i+1} Marks={student[i]} --> Good"+ v)
    elif student[i]>=40:
        vc+=1
        print(f"Student-{i+1} Marks={student[i]} --> Average"+v)
    elif 0<=student[i]<=39:
        vc+=1
        fc+=1
        print(f"Student-{i+1} Marks={student[i]} --> Fail" +v+v+v)
    else:
        print("Invalid mark"+v)

print(f"Total Valid Students: {vc}"+v)
print(f"Total Failed Students: {fc}"+v)

