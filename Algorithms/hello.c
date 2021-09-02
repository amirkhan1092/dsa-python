#include<stdio.h>
#include<conio.h>

int main()
{
    float b1, h1, b2, h2, value;
    scanf("%f %f", &b1, &h1);
    scanf("%f %f", &b2, &h2);
    float t1, t2;
    t1 = (b1*h1)/2;
    t2 = (b2*h2)/2;
   
    if (t1 > t2)
        printf("%.6f", t1);
    else
        printf("%.6f", t2);



    return 0;

}