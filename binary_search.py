def binary_search(lst, x):
    lst.sort()
    mid = len(lst)/2
    mid_value = lst[mid]
    if x==mid_value:
        print True
    if x<mid_value:
        lst = lst[:mid]
        binary_search(lst,x)
    elif x>mid_value:
        lst = lst[mid:]
        binary_search(lst,x)
    
binary_search([3,5,1,2,6,7,9,11],2)
