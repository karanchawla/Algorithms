def quicksort(lst):
	if len(lst)<=1: 
		return lst
	c = 0 #number of comparisons
	lst,i,j = partition(lst,0,len(lst))	
	lst[:i-1] = quicksort(lst[:i-1])
	lst[i:j+1] = quicksort(lst[i:j+1])
	return lst

def partition(lst,l,r):
	p = lst[l]
	i = l+1
	for j in range(l+1,r):
		print lst[j]
		if lst[j]<p:
			lst[i], lst[j] = lst[j], lst[i]
			i+=1
	lst[l],lst[i-1] = lst[i-1],lst[l]
	#print lst
	return lst,i,j

lst = [5,4,1,7,6,8,3,11,32,54,65,88,37,3234,67,988,145,667]
print quicksort(lst)
