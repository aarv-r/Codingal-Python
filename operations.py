a=[1,3,2,4,6,8,7]
print(a)
sum=0
avg=0
for i in a:
    sum+=i

avg=sum/len(a)
print("sum=", sum)
print("avg=", avg)
print(min(a))
print(max(a))
