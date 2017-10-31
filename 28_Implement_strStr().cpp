#include<iostream>
#include <string>
using namespace std;
using  std::string;
int strStr(string haystack, string needle) {
	int haylen = haystack.length();
	int needlelen = needle.length();
	int i, j, k;
	int flag = 0;
	for (i = 0; i < haylen - needlelen+1; i++){
		flag = 0;
		for (j = 0; j < needlelen; j++){
			if (needle[j] == haystack[i+j])
				continue;
			else{
				flag = 1;
			}
				
		}
		if (flag == 0){
			return i;
		}
	}
	if (haystack == needle){
		return 0;
	}
	return -1;
}
int main(){
	string haystack = "helloabcworld";
	string needle = "abc";
	int d;
	d = strStr(haystack, needle);
	cout << d<<"\n";
	//printf("helloworld");
	system("pause");
	return 0;
}