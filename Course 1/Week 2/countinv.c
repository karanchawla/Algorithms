#include <stdio.h> 
#include <stdlib.h>

int count = 0;

void Merge(int *A, int *L, int leftCount, int *R, int rightCount){
	int i,j,k;
	i = 0; j = 0; k = 0;

	while (i<leftCount && j <rightCount){
		if(L[i] < R[j]){
			A[k] = L[i];
			k++; i++;
		}else{
			A[k] = R[j];
			k++; j++;
			count += leftCount -i;
		}
	}
	while(i<leftCount) A[k++] = L[i++];
	while(j<rightCount) A[k++] = R[j++];
}

void MergeSort(int *A, int n){
	int mid, i, *L, *R;
	if(n<2) return;

	mid = n/2;

	L = (int*)malloc(mid*sizeof(int)); 
	R = (int*)malloc((n- mid)*sizeof(int));

	for(i=0;i<mid;i++) L[i] = A[i];
	for(i=mid;i<n;i++) R[i-mid] = A[i];

	MergeSort(L,mid);
	MergeSort(R,n-mid);
	Merge(A,L,mid,R,n-mid);
	free(L);
	free(R);
}

int main(){

	int A[] = {3,1,2,4,6,5,7,10,9};
	int i, numberOfElements;

	numberOfElements = sizeof(A)/sizeof(A[0]);

	MergeSort(A,numberOfElements);
	
	for(i = 0;i < numberOfElements;i++) printf("%d ",A[i]);
	
	printf("The number of inversions in the given array are: %d\n", count );

	return 0;
}







































/*int count = 0;

int * merge_sort( int * lst);

int * merge(int * l, int * r);

int * merge_sort(int * lst){
	int len_lst = sizeof(lst)/sizeof(lst[0]);
	if (len_lst <2){
		return lst;
	}
	int m = len_lst/2;
	int left[100];
	int right[100];
	for(int i=0;i<m;i++){
		left[i] = lst[i];
	}
	for (int j=m;j<len_lst;j++){
		right[j] = lst[j];
	}

	return merge(left, right);
}

int * merge(int * l, int * r){
	int result[100];
	int i = 0;
	int j = 0;
	int k =0;
	int length_l = sizeof(l)/sizeof(l[0]);
	int length_r = sizeof(r)/sizeof(r[0]);
	while (i < length_l && j < length_r){
		if (l[i] < r[j]){
			result[i] = l[i];
			i++;
		}else {
			result[j] = r[j];
			j++;
			count = count + length_l-i;
		}
	}
	//copy remaining arrays to result
	k = sizeof(result)/sizeof(result[0]);
	for (int i = i;i<length_l;i++){
		result[k] = l[i];
	}
	k = sizeof(result)/sizeof(result[0]);
	for (int i = j;i<length_l;i++){
		result[k] = r[j];
	}
	return *result;

}

int main(){
	int lst[4] = {1,3,2,4};
	int *result;
	*result = merge_sort(lst);
	for(int i =0;i<4;i++){
		printf("%d\n", *(result+i));
	}
	return 0;
}*/

