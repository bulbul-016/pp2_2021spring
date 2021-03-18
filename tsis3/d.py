if __name__=='__main__':
    text=input().split()
    lisst=list(text)
    for i in range(len(lisst)):
        for j in range(i):
            if lisst[i]>lisst[j]:
                print(lisst[i])