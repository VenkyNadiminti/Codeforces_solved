for i in range(int(input())):
    n=int(input())
    ans=[]
    c=0
    if n <= 9:
        print(1)
        print(n)
    else:
        while n!=0:
            if n<=9:
                c+=1
                ans.append(n)
                break
            div='1'+('0'*(len(str(n))-1))
            tmp=n//int(div)
            ans.append(int(div)*tmp)
            n=n%int(div)
            c+=1
        print(c)
        for i in ans:
            print(i,end=" ")
        print()
