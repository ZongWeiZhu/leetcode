#include <stdio.h>
#include <stdlib.h>
using namespace std;
int* ba(int* nums, int numsSize, int target) {
	int min = 2147483647;
	int i = 0;
	for (i = 0; i < numsSize; i++) {
		if (nums[i] < min)
			min = nums[i];
	}
	int max = target - min;
	int len = max - min + 1;
	int *table = (int*)malloc(len*sizeof(int));
	int *indice = (int*)malloc(2 * sizeof(int));
	for (i = 0; i < len; i++) {
		table[i] = -1;
	}
	for (i = 0; i < numsSize; i++) {
		if (nums[i] - min < len) {
			printf("target - nums[i] - min %d \n", target - nums[i] - min);
			if (table[target - nums[i] - min] != -1) {
				//printf("%d \n", table[target - nums[i] - min]);
				indice[0] = table[target - nums[i] - min];
				indice[1] = i;
				int j;
				for (j = 0; j < 4; j++){
					printf("table : %d", table[j]);
				}
				return indice;
			}
			table[nums[i] - min] = i;
			printf("%d \n", table[nums[i] - min]);
		}
	}
	free(table);
	return indice;
}
int main4(){
	int a[4] = { 1, 3, 2, 7 };
	int b = 4;
	int c = 9;
	int* d;
	d = ba(a, b, c);
	//printf("12312321");
	printf("%d,%d", d[0], d[1]);
	system("pause");
	return 0;
}