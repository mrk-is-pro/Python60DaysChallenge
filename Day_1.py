name=input("Full Name:")
mail=input("Email:")
mobile=input("Mobile:")
age=int(input("Age:"))
count=0
if " " in name and name[0]!=" " and name[len(name)-1]!=" ":
    count+=1
if mail.count("@")==1 and mail.count(".")>=1 and mail[0]!="@":
    count+=1
if len(mobile)==10 and mobile.isdigit() and mobile[0]!=".":
    count+=1
if 18<=age<=60:
    count+=1
if count==4:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")

