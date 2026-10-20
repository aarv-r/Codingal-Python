import array as a
num=a.array( 'i', [1,2,3,4,4,4,5] )
print(num)
print(num.count(4))
num.insert(2,6)
print(num)
num.reverse()
print(num)