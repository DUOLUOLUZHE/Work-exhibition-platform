#include "head.h"

int number = 0;
int a = 0xFE;

void main(){
		P2 = a;
		while(1){
			Timer0Init();
			number = button();
		}
}

void plan() interrupt 1
{		
		static int time = 0;
		TL0 = 0x40;		
		TH0 = 0xA2;	
		time++;
		if(time>=500){
			time = 0;
			if(number == 1){
				P2 = _crol_(a,1);
			}
			if(number == 2){
				P2 = _cror_(a,1);
			}
		}

}