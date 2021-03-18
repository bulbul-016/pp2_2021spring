if __name__ == '__main__':
    text = input().split()
    for i, v in enumerate(text):
        if int(v)%2==0:
            print(int(v), end=' ')

#1 2 2 3 4 5
#2 2 4 