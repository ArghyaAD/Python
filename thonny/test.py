n=int(input("enter the range :"))
i=1
sum=0
while(i<=n):
    current_number=i
    while(i>=1):
        position=int(i%10)
        sum+=(position**3)
        i=int(i/10)
    if current_number==sum:
        print(current_number)
    i=current_number+1