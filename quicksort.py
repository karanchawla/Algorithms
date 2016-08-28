def quicksort(lst):
	if len(lst)<=1: 
		return lst
	p = median(0,len(lst),lst)
	p,lst[0] = lst[0],p
	lst,i,j = partition(lst,0,len(lst),p)	
	lst[:i-1] = quicksort(lst[:i-1])
	lst[i:j+1] = quicksort(lst[i:j+1])
	#print c
	return lst

def choose_pivot(x,l,r,lst): 
	if x==0:
		return lst[l]
	if x==1:
		return lst[r-1]
	if x==2:
		mid = len(lst)//2
		mid_element = lst[mid]
		median_array = [l,r,mid_element]
		median_array.sort()
		return median_array[1]

def median(l,r,lst):
	mid = len(lst)//2
	mid_element = lst[mid]
	median_array = [l,r,mid_element]
	median_array.sort()
	return median_array[1]

def partition(lst,l,r,p):
	global c 
	#p = lst[r-1]
	i = l+1
	for j in range(l+1,r):
		#print lst[j]
		if lst[j]<p:
			lst[i], lst[j] = lst[j], lst[i]
			i+=1
	lst[l],lst[i-1] = lst[i-1],lst[l]
	c += r-1
	#print lst
	print i,j
	return lst,i,j

with open('QuickSort.txt') as f:
	array = []
	for line in f:
		array.append(int(line))

#array = [3,11,2,4,67,0,23,54,19]
global c
c = 0
quicksort(array)
print(c)
