Name="Makineni Ruthvik Krishna"

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

print("\n\n---Base Classification---\n ")
print(f"Very Light: {very_light}")
print(f"Normal Load: {normal_load}")
print(f"Heavy Load: {heavy_load}")
print(f"Overload: {overload}")
print(f"Invalid Entries: {invalid_entries}")
