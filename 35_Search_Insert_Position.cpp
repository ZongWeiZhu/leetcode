#include<stdio.h>
//优先级 先判断相等的情况 然后判断是否最后 然后判断< >，最后还要判断数组是否的单一的，可以优化在一块
int searchInsert(int* nums, int numsSize, int target) {
    int i;
	int count=0;
	int flag=0;
	for(i=0;i<numsSize;i++)
	{
		if(target==nums[i]){
			flag=i;
			count=1;
			break;
		}
		if(i==numsSize-1){
			if(target>nums[i]){
			flag=i+1;
			count=1;
			break;
		}	
		}
		else{
		if(target>nums[i] && target<nums[i+1]){
			flag=i+1;
			count=1;
			break;
		}
		}
	}
	if(numsSize==1){
		if(target<=nums[0]){
			flag=0;
		}
		else{
			flag=1;
		}
	}
	return flag;
}
int main()
{
	int a[2]={1,3};
	int b = 2;
	int c = 4;
	int d;
	//d = removeDuplicates(a,b);
	d= searchInsert(a,b,c);
	printf("%d",d);
	return 0;
}