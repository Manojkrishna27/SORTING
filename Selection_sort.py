#SELECTION SORT

arr=[1,2,1,3,4,2]             #take a array
n=len(arr)                     #take arrays length
for i in range(n):              # loop run until it reaches array length
    min1=i                       #take min as temp of i position
    for j in range(i+1,n):       # j start from next to  i and compare all values
        if arr[j]<arr[min1]:
            min1=j
    temp=arr[i]                #manipluate the array
    arr[i]=arr[min1]
    arr[min1]=temp
print(arr)