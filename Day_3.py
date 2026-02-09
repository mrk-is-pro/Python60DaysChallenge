student=[]
name="ruthvik"
x=input("Enter the Name of the person entering Marks:")
if x==name.lower():
    v="?"
else:
    v=""
n=int(input("Enter No.of Students:"))
for i in range(n):
    student+=[int(input(f"Enter Marks of Student-{i+1}: "))]
vc=0
fc=0
for i in range(n):
    if 90<=student[i]<=100:
        vc+=1
        print(f"Student-{i+1} Marks = {student[i]} --> Excellent" + v)
    elif 75<=student[i]<=89:
        vc+=1
        print(f"Student-{i+1} Marks = {student[i]} --> Very Good"+ v)
    elif 60<=student[i]<=74:
        vc+=1
        print(f"Student-{i+1} Marks = {student[i]} --> Good"+ v)
    elif 40<=student[i]<=59:
        vc+=1
        print(f"Student-{i+1} Marks = {student[i]} --> Average"+v)
    elif 0<=student[i]<=39:
        vc+=1
        fc+=1
        print(f"Student-{i+1} Marks = {student[i]} --> Fail" +v+v+v)
    else:
        print(f"Student-{i+1} Marks = {student[i]} --> Invalid"+v)

print(f"Total Valid Students: {vc}"+v)
print(f"Total Failed Students: {fc}"+v)

