#include<stdio.h>
int main()
{
    int a;
    a=10;
    a= ++a + ++a + ++a;
    printf("%d", a);
}