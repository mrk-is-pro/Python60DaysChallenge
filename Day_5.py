Name="Makineni Ruthvik Krishna"
L=len(Name)-Name.count(" ")
PLI=L%3

N=int(input("Enter No. of Elements in the List: "))
Given=[0]*N
for i in range(N):
    Given[i]=int(input(f"Enter Element-{i+1}: "))

very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entries=[]

for i in range(N):
    if Given[i]<0:
        invalid_entries+=[Given[i]]
    elif Given[i]<6:
        very_light+=[Given[i]]
    elif Given[i]<26:
        normal_load+=[Given[i]]
    elif Given[i]<61:
        heavy_load+=[Given[i]]
    else:
        overload+=[Given[i]]

affected_items=len(very_light)
very_light=[]

count=len(normal_load)+len(heavy_load)+len(overload)

print("\n\nNo. of Valid Weights:",count)
print("No. of Affected Items:",affected_items)
print("L=",L," and PLI=",PLI)
print("\n---Final Lists---\n ")
print(f"Normal Load: {normal_load}")
print(f"Heavy Load: {heavy_load}")
print(f"Overload: {overload}")
print(f"Invalid Entries: {invalid_entries} ")

