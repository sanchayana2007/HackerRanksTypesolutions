#include<stdio.h>

int fibo(int a)
{
		if ((a==1) || (a == 2)){
		return 	1;}
		else{
		return fibo(a-2) + fibo(a-1); }
}



int main(int argc, char **argv)
{
		printf("%d",fibo(4));
	
	
}