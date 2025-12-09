def recrusiveinsertion_sort(arr,n):
    if n<=1:
        return
    
    recrusiveinsertion_sort(arr,n-1)

    last=arr[n-1]
    j=n-2

    while j>=0 and arr[j]>last:
        arr[j+1]=arr[j]
        j-=1

    arr[j+1]=last
arr=[2,5,6,3,1,4]
recrusiveinsertion_sort(arr,len(arr))
print(arr)