n=int(input())
for i in range(n):
    s1=input()
    if len(s1)>10:
        x=f"{s1[0]}{len(s1)-2}{s1[len(s1)-1]}"
        print(x)
    else:
        print(s1)
