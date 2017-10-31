#include <stdio.h>
#include <stdlib.h>
int reverse(int x) {
	int ans = 0;
	while (x) {
		int temp = ans * 10 + x % 10;
		if (temp / 10 != ans)
			return 0;
		ans = temp;
		x /= 10;
	}
	return ans;
}
int main17(){
	int a = 123;
	int d;
	d = reverse(a);
	printf("%d\n", d);
	//printf("helloworld");
	system("pause");
	return 0;
}