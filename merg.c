#include<stdio.h>
#define sz 10
void main()
{
        int a[sz]={10,9,8,7,6,5,4,3,2,1};
	void merg (int [],int,int);
        int i,lb=0,ub=9;
        merg(a,lb,ub);
	for(i=0;i<=ub;i++)
	printf("%d\t",a[i]);
}
void merg(int a[],int lb,int ub)
{

	int m;
	void demerg (int[],int,int,int,int);
        if(lb<ub)
{
	 m=(lb+ub)/2;
        merg ( a,lb,m);
	merg (a,m+1,ub);
        demerg (a,lb,m,m+1,ub);
}
}
void demerg (int a[],int llb,int lub,int rlb,int rub)
{
	int i,temp[sz],t1,t2;
      for(i=0,t1=llb,t2=rlb;t1<=lub&&t2<=rub;i++)
	      temp[i]=a[t1]>a[t2]?a[t2++]:a[t1++];

	        while(t1<=lub)
		temp[i]=a[t1++],i++;

		while(t2<=rub)
		temp[i]=a[t2++],i++;

	for(i=0,t1=llb;t1<=rub;t1++,i++)
         a[t1]=temp[i];
}
