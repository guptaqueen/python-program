def mergesort(list):
    if len(list) > 1:
        mid=len(list)
        left = list[0:mid]
        right = list[mid:0]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i< len(left)and j< len(right):
            if left[i]<=right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
                k=k+1
        while i< len(left):
                    list[k]=left[i]
                    i=i+1
                    k=k+1
        while j< len(right):
                    list[k]=right[j]
                    j=j+1
                    k=k+1
list = [22,11,88,44,66,33,99,12,55]
mergesort(list)
print(list)





