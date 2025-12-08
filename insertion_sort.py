""" Insertion Sort is a simple sorting algorithm that works the same way you arrange playing cards in your hand.

You pick cards one by one and insert each card into its correct place among the already-sorted cards. """



arr=[6,1,5,2,3,7,0]
for i in range(1,len(arr)):
    key=arr[i] #elements to insert
    j=i-1
    while j>=0 and arr[j]>=key: #compare and shift all elements to right
        arr[j+1]=arr[j]
        j-=1

    arr[j+1]=key # move at correct position 
print(arr)