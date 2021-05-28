x=int(input())
for i in range(x):
    a=int(input())
    s=list(input().split())
    c=0
    for i in s:
        if i=="cookie":
            c+=1
        else:
            c=0

        if c==2:
            break
    if c==0:
        print("YES")
    else:
        print("NO")