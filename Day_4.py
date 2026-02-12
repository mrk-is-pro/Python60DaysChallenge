
Name=input("Enter Your Name: ")

N=int(input("Enter No. of Elements in the List: "))
Given=[0]*N
for i in range(0,N):
    Given[i]=input("Enter Element: ")
Numbers=[]
Strings=[]
countit=0
for i in range(0,len(Given)):
    if Given[i].isdigit():
        Numbers+=[int(Given[i])]
    elif type(Given[i])==str:
        if Given[i]!="":
            Strings+=[Given[i]]
        else:
            countit+=1
    else:
        print("List Contains Elements other than Numbers and Strings")
Nremove=0
Sremove=""
if len(Name)%2==0:
    Nremove=Numbers[0]
    Sremove=Strings[0]
    del Numbers[0]
    del Strings[0]
else:
    Nremove=Numbers[-1]
    Sremove=Strings[-1]
    del Numbers[-1]
    del Strings[-1]

print("\nStrings List:",Strings)
print("Numbers List:",Numbers)
print("\nTotal Strings:",len(Strings))
print("Total Numbers:",len(Numbers))
print("\nRemoved Element from Strings:",Sremove)
print("Removed Element from Numbers:",Nremove)
if Name.lower() == "ruthvik":
    print("Ignored Empty Strings(\"\"):",countit)
