def recursivebubble(arr,n):
    if n==1: #base condition
        return
    for i in range(n-1):
        if arr[i]<arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]     # swap
    recursivebubble(arr,n-1)      # recursion

arr=[2,1,7,5,3,4]
recursivebubble(arr,len(arr))
print(arr)