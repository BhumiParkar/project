def bubble_sort(array,size):
    for i in range(size):
        Swaps=0;
        for j in range(0,size-i-1):
            if(arr[j]>arr[j+1]):
               temp=arr[j]
               arr[j]=arr[j+1]
               arr[j+1]=temp
               swaps=1;
            if(swaps==0):
                break
        

arr=[66,44,82,16,20]
n=len(arr)
print("array before sorting:",arr)
bubble_sort(arr,n)
print("array after sorting:",arr)
