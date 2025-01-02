nums = [0,1,2,2,3,0,4,2]
val = 2
kold = len(nums)
knew = kold
nums2 = []
k=0
for i in range(len(nums)):
    if nums[i] != val:
        print(nums[i])
        knew -= 1
        nums2.append(nums[i])
nums = nums2
k = knew
print(nums)
print(knew)