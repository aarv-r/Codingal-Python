a={"Aarav": 5, "Ramesh": 3, "Suresh": 5, "Nihil": 2}
k=5
count=0
for i in a:
    if a[i]==k:
        count+=1
print("The number of students who scored", k, "marks is", count)