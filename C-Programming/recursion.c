#include<stdio.h>
int factorial(int);
int main()
{
    int n, out;
    n = 5;
    out = factorial(n);
    printf("Factorial of %d is %d", n, out);
    return 0;
}

int factorial(int num)
{   
    if(num == 0)
            return 1;
    
    return (num * factorial(num-1));
}
