def fibonacci(num):
    if num<=1:
        return num
    else:
        return (fibonacci(num-1)+fibonacci(num-2))


nterm=int(input("range:"))
if nterm<=0:
    print("enter a positive integer:")
else:
    print("series is: ")
    for i in range(nterm):
        print(fibonacci(i))