#include<stdio.h>
void main()
{
  FILE *p;
	int a,b;
	char c[10];
	p=fopen("/home/vipin/hello.txt","w");
	printf("enter age GDP and name");
        scanf("%d%d%s",&a,&b,c);
	fprintf(p,"AGE=%d      GDP=%d  NAME=%s",a,b,c);
	fclose(p);
}
