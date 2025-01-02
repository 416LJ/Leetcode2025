nums =[2,14,18,22,22]
for num in nums:
    count = nums.count(num)
    print(count)
    if count >= 2:
        print("True")
    else:
        print("False")