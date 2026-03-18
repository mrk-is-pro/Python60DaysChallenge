n="Makineni Ruthvik Krishna"
l=len(n)-n.count(" ")

N=int(input("Enter No. of Elements in the List: "))
a=[0]*N

for i in range(N):
    a[i]=int(input(f"Enter Element-{i+1}: "))

d={"efficient":[],"moderate":[],"high":[],"invalid":[]}

for i in range(N):
    x=a[i]
    if x<0:
        d["invalid"]+=[x]
    elif x<=50:
        d["efficient"]+=[x]
    elif x<=150:
        d["moderate"]+=[x]
    else:
        d["high"]+=[x]

v=[x for x in a if x>=0]

t=sum(v)
b=len(v)

s=(t,b)

r=""

if t>600:
    r="Energy Waste Detected (High Total)"
elif len(d["high"])>3:
    r="Energy Waste Detected (Too Many High Readings)"
elif abs(len(d["efficient"])-len(d["moderate"]))<=1:
    r="Efficient Campus (Balanced)"
else:
    r="Moderate Usage (Normal)"

print("\n\n---Energy Analysis---")

print(f"\nTotal Consumption: {s[0]}")
print(f"Buildings: {s[1]}")

print("\n---Categories---\n")
print(f"Efficient: {d['efficient']}")
print(f"Moderate: {d['moderate']}")
print(f"High: {d['high']}")
print(f"Invalid: {d['invalid']}")

if l%2==0:
    print(f"\nInvalid Entries: {len(d['invalid'])}")
else:
    print(f"\nHigh Consumption Count: {len(d['high'])}")

print(f"\nResult: {r}")