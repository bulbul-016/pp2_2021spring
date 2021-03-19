massive=list(map(int, input().split()))
massive.sort()
cnt=0
for i in range(len(massive)):
    for j in range(i):
        if massive[i]==massive[j]:
            cnt=cnt+1
print(cnt)