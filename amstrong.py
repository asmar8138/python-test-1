num=int(input("enter the number: "))
sum=0
temp=num
while temp!=0:
    digit=temp%10
    sum=sum+digit**3
    temp //=10
if num==sum:
    print("amstrong")
else:
    print("not amstrong")