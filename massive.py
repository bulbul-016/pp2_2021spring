massive=list(map(int, input().split()))
cnt=0
for i in range(len(massive)):
    for j in range(i):
        if massive[i]==massive[j]:
            cnt=cnt+1
print(cnt)

#1 2 2 1 3 4 5 1
#4