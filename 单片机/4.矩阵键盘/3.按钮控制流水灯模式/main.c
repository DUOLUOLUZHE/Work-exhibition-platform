#include "head.h"

int off = 0;
int dat = 0;

void main(){
	
	init();
	while (1){
		switch (off){
			case 1:
				format1();
				break;
			case 2:
				format2();
				break;
			case 3:
				format3();
				break;
			case 4:
				format4();
				break;
		}
	}
}

int T = 0;
void time_look() interrupt 1
{
	TH0 = 64535/256;
	TL0 = 64535%256;
	T++;
	if (T>=200){
		T = 0;
		if(dat = detection()){
			off = dat;
		}
	}

}

