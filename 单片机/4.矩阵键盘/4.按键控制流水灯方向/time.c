#include "head.h"


void Delay1ms(number)		//@24.000MHz
{
	unsigned char i, j;
	while(number){
		i = 24;
		j = 85;
		do
		{
			while (--j);
		} while (--i);
	}
}

void Timer0Init()		//1??@24.000MHz
{

	TMOD &= 0xF0;		//???????
	TL0 = 0x40;		
	TH0 = 0xA2;		
	TF0 = 0;		//??TF0??
	TR0 = 1;		//???0????
}
