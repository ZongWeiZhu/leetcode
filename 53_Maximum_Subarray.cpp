#include <stdio.h>
#include <stdlib.h>
int maxSubArray(int* nums, int numsSize) {
	int max = nums[0];
	int i,j;
	int sum = 0;
	for (i = 0; i < numsSize; i++){
		sum = nums[i];
		//子序列是否大于最大值
		for (j = i + 1; j < numsSize; j++){
			sum = sum + nums[j];
			if (sum > max){
				max = sum;
			}
		}
		//判断单个是否大于最大值
		if (nums[i]>max){
			max = nums[i];
		}
	}
	return max;
}
int main(){
	int a[9] = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
	int b = 9;
	int c = 3;
	int d;
	d = maxSubArray(a, b);
	printf("%d \n", d);
	printf("helloworld");
	system("pause");
	return 0;
}