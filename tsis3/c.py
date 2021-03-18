if __name__=='__main__':
    cnt=0
    text=input().split()
    for i, v in enumerate(text):
        if int(v)>0:
            cnt+=1
    print(cnt)
#1 -2 3 -4 5 6
#4