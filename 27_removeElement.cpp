#include <stdio.h>
#include <stdlib.h>
int removeElement(int* nums, int numsSize, int val) {
	int i = 0;
	int j = 0;
	int k = 0;
	int count = 0;
	for (i = 0; i < numsSize-j; i++){
		if (nums[i] == val){
			k = nums[i];
			nums[i] = nums[numsSize - j-1];
			nums[numsSize - j-1] = k;
			j++;
			i--;
		}
		else{
			count++;
		}
	}
	if (j == numsSize){
		nums = NULL;
		count = 0;
	}
	return count;
}
int main(){
	int a[1] = {2};
	int b = 1;
	int c = 3;
	int d;
	d = removeElement(a, b, c);
	printf("%d \n", d);
	system("pause");
	return 0;
}