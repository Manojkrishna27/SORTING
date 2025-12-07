""" BUBBLE SORT """
""" Bubble Sort is a method of arranging numbers in order by repeatedly comparing two neighboring numbers and swapping them if they are in the wrong order.
You keep doing this again and again until everything becomes sorted. """

arr=[1,3,4,6,5,2,8]

n=len(arr) 

for i in range(n):
    

    swapped=False  # to check if any swapping happened in this pass

    for j in range(0,n-i-1): # like a bubble compareing each element with neighbour

        if arr[j]>arr[j+1]:   # if the left number is bigger, swap them

            arr[j],arr[j+1]=arr[j+1],arr[j]  # swapping
            swapped=True       #  swap happened

    if not swapped: 
        break       # if no swap happen it mean it is already started so break

print(arr)