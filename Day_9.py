import copy

n="Makineni Ruthvik Krishna"
l=len(n)-n.count(" ")

rno=input("Enter Register Number: ")
num=int(rno[-2:])

def generate_data():
    return [
        {"id":1,"data":{"files":["a.txt","b.txt"],"usage":500}},
        {"id":2,"data":{"files":["c.txt"],"usage":300}}
    ]

def replicate_data(a):
    assign=a
    shallow=a[:]
    deep=copy.deepcopy(a)
    return assign,shallow,deep

def modify_data(a):
    if num%2==0:
        a[0]["data"]["files"].append("new.txt")
    else:
        if a[0]["data"]["files"]:
            a[0]["data"]["files"].pop()

    a[0]["data"]["usage"]=a[0]["data"]["usage"]+50

    if a[1]["data"]["files"]:
        a[1]["data"]["files"].pop()

    return a

def check_integrity(before,after,shallow,deep):
    leak=0
    safe=0

    if before!=after:
        leak=leak+1
    else:
        safe=safe+1

    if before==deep:
        safe=safe+1

    f1=set()
    f2=set()

    for i in after:
        for j in i["data"]["files"]:
            f1.add(j)

    for i in shallow:
        for j in i["data"]["files"]:
            f2.add(j)

    overlap=len(f1 & f2)

    if before[0]["data"]!=after[0]["data"]:
        print("Inner level changed")
    else:
        print("Only outer level changed")

    return (leak,safe,overlap)

before=generate_data()
before_copy=copy.deepcopy(before)

print("\n---Before---\n",before)

assign,shallow,deep=replicate_data(before)

assign=modify_data(assign)

print("\n---After Assignment---\n",assign)
print("\n---Original---\n",before)
print("\n---Shallow Copy---\n",shallow)
print("\n---Deep Copy---\n",deep)

t=check_integrity(before_copy,before,shallow,deep)

print("\n---Integrity Summary---")
print("Leakage, Safe, Overlap:",t)

if l%2==0:
    print("Observation: Data changed due to shared reference")
else:
    print("Observation: Deep copy protected original data")

print("\nInsight: Data corruption occurs when original data changes due to shared references.")