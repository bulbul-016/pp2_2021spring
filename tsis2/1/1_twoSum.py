nums=list[int(input())]
b=int(input())
i=0
for i in nums:
    if nums[i]+nums[i+1]==b:
        print('['+str(i)+','+str[i+1]+ ']')
    i=i+1
    