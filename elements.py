arr = []
ele = int(input("how many elements:"))
for i in range(0,ele):
    arr.append(int(input("enter the element ")))
print(arr)

largest = arr[0]
second = 0
for i in arr:
    largest = max(largest,i)
print ("Largest number is: ",largest)
for i in arr:
    if i!=largest:
        second = max(second,i)
print("second large number is: ",second)