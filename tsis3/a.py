if __name__ == '__main__':
    text = input().split()
    for i, v in enumerate(text):
        if i % 2==0:
            print(v, end=' ')
#1 2 3 4 5
#1 3 5 