#include <stdio.h> 

int partition(int A[], int l ,int r);

void QuickSort(int A[], int left, int right);

int partition(int A[], int l, int r){
	int p = A[0];
	int i = l+1;
	int temp1 = 0;
	int j=l+1;
	for(j=l+1;j<r;j++){
		int temp = 0;
		if (A[j]< p){
			temp = A[i];
			A[i] = A[j];
			A[j] = temp;
			i+=1;
		}else continue;
	}
	temp1 = p;
	A[l] = A[i-1];
	A[i-1] = temp1;
	//for(int k=0;k<4;k++) printf("%d", *(A+k));
	//printf("%d%d\n", i,j );
	//printf("\n");
	return j;
}	

void QuickSort(int A[], int left, int right){
	
	int j=0;

	if ((right-left)>0){
		j = partition(A,left,right);
		QuickSort(A, left, j-1);
		QuickSort(A, j+1, right);
	}
}

int main(){
	int A[] = {0,1,5,8,9,2,6};
	int right = sizeof(A)/sizeof(A[0]);
	int z = 0;
	QuickSort(A,0,9);
	for(int i=0;i<right;i++) printf("%d \t", *(A+i) );
}