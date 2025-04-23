nums = [3,0,1]
nums.sort()
max_num = max(nums)

for i in range(0,max_num+1):
    if i not in nums:
        print(i)