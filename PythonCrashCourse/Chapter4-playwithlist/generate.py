for i in range(1,21):
    print(i)

nums = [value for value in range(1,1000001)]
for num in nums:
    print(num)
print(min(nums))
print(max(nums))
print(sum(nums))

nums = [value for value in range(1,20,2)]
for num in nums:
    print(num)

nums = [value for value in range(3,31,3)]
for num in nums:
    print(num)

nums = [value**3 for value in range(1,11)]
for num in nums:
    print(num)