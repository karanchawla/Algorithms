def merge(lst):
    if len(lst)<=1: #handles empty arrays or arrays with single values
        return lst
    mid = len(lst)//2
    left = lst[0:mid]
    right = lst[mid:]
    left = merge(left)
    right = merge(right)
    i=0
    j=0
    k=0
    while i < len(left) and j < len(right):
        if left[i]<=right[j]: #handles equal cases
            lst[k] = left[i]
            i+=1
        elif left[i]>right[j]:
            lst[k] = right[j]
            j+=1
        k +=1
    while i < len(left):
                lst[k] = left[i]
                i+=1
                k+=1
    while j < len(right):
                lst[k] = right[j]
                j+=1
                k+=1
    return lst

array = [2,5,1,2,90,15,56,12,34]
print merge(array)
