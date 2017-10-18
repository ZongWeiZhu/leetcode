#include<stdio.h>
//找出相同的元素之后把数组整体向前移动 然后把该元素放到数组的倒数numsSize-K-1
int removeDuplicates(int* nums, int numsSize) {
    int i=0;
	int count=0;
	int j=0;
	int k=0;
	int temp;
	for(i=0;i<numsSize-k-1;i++){
		if(nums[i]==nums[i+1]){
			temp = nums[i+1];
			for(j=i+2;j<numsSize;j++)
			{
				nums[j-1]=nums[j];
			}
			nums[numsSize-1-k] = temp;
			k++;
			i--;
		}
	}
	return numsSize-k;
	
}
int main()
{
	int a[11]={1,1,2,2,3,4,4,5,6,6,7};
	int b = 11;
	int d;
	d = removeDuplicates(a,b);
	printf("%d",d);
	return 0;
}