Id=input("ID:")
Email=input("Email:")
password=input("Password:")
ref=input("Referral:")
count=0
if Id[:3]=="CSE" and Id[3]=="-" and Id[len(Id)-3:].isdigit():
    count+=1
if Email.count("@")==1 and Email.count(".")>=1 and Email[0]!="@" and Email[len(Email)-1]!="@" and Email[len(Email)-4:]==".edu":
    count+=1
if len(password)>=8 and password[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and (password.count('0') or password.count('1') or password.count('2') or password.count('6') or password.count('7') or password.count('8') or password.count('3') or password.count('4') or password.count('5') or password.count('9')):
    count+=1
if ref[:3]=="REF" and ref[3] in "0123456789" and ref[4] in "0123456789" and ref[5]=="@" :
    count+=1
if count==4:
    print("APPROVED")
else:
    print("REJECTED")
print(count)