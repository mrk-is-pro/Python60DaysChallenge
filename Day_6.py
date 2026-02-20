N=int(input("Enter No. of Elements in the List: "))
Given=[0]*N
for i in range(N):
    Given[i]=int(input(f"Enter Element-{i+1}: "))
Invalid=0
Total=0
Dup=0
for i in range(N):
    if Given[i]<=0:
        Invalid+=1
        break;
for i in range(N):
    for j in range(i+1,N):
        if Given[i]==Given[j]:
            Dup+=1

Category=""
reco=""
if Invalid==0:
    Total=sum(Given)
    if Total>3600:
        if Dup>0:
            Category="Too Long And Repetitive"
            reco="Try to reduce the no of songs in your playlist by removing repetitive songs!!"
        else:
            Category="Too Long"
            reco="Try to reduce the number of Songs in your playlist"
    elif Total<300:
        if Dup>0:
            Category="Too Short And Repetitive"
            reco="Try to add more songs of Different variety to the Playlist!!"
        else:
            Category="Too Short"
            reco="You Should add more songs to Your playlist!!"
    elif 300<=Total<=3600:
        if Dup>0:
            Category="Repetitive"
            reco="Try to Listen to a variety of Songs"
        else:
            Category="Balanced"
            reco="Perfect Playlist!! You have Great Taste!!"
    else:
        Category="Irregular"
        reco="How did you even get this??"

    print("\n\n---Playlist Analysis---")
    print(f"\nTotal Duration: {Total}")
    print(f"Songs: {len(Given)}")
    print(f"Category: {Category} Playlist")
    print(f"Recommendation: {reco}\n")

else:
    Category="Invalid"
    print(f"\nCategory: {Category} Reported!!!")
    print("---Analysis Stopped---")