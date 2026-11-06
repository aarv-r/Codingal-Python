class pair_elements:
    def twosum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target-num in lookup:
                return (lookup[target-num], i)
            lookup[num] = i
value=int(input("Enter sum for which you want to make this search :"))
obj=pair_elements()
print(obj.twosum((10,20,30,40,50,60,70), value))
