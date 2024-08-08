#include "head.h"

void sleep(number)		//@24.000MHz
{
	unsigned char i, j;
	while(number--){
		i = 24;
		j = 85;
		do
		{
			while (--j);
		} while (--i);
	}
}