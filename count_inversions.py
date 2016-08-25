def count_inversion(lst):
	return merge_count_inversions(lst)

def merge_count_inversions(lst):
	if len(lst)<=1:
		return lst, 0
	mid = len(lst)//2
	left,a = merge_count_inversions(lst[:mid])
	right,b = merge_count_inversions(lst[mid:])
	result,c = count_split_inversion(left,right)

	return result,a+b+c

def count_split_inversion(left,right):
	i=0
	j=0
	result = []
	c = 0
	while i< len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i+=1
		else: 
			result.append(right[j])
			c+=1
			j+=1

	result += left[i:]
	result += right[j:]

	return result,c

lst = [5,4,3,2,1]
print count_inversion(lst)
