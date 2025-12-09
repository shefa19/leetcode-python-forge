nums = [100]

result = 0

for i, n in enumerate(nums):
    if i % 2 == 0:
        result += n
    else:
        result -= n
        
print(result)