from collections import defaultdict

#defualt dict behaves like ordinary dict but when you try to access non existent key it 
#throw key error 
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
nums['three'] = 3
print(nums['four'])
