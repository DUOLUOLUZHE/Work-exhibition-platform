#include <REGX52.H>
#include "time.h"
#include "button.h"
#include "Nixie.h"
#include "voice.h"
#include "Timer0.h"
#include "music_table.h"



sbit BEEP = P2^5;
int TL_TH;
unsigned int NEW_TL;
unsigned int NEW_TH;



void main(){
		int i = 0;
		Timer0Init();
			while(1){
					for(i = 0;i < xiaoxingxing_len;i++){
							TL_TH = music_table(xiaoxingxing[i]);
							NEW_TL = TL_TH%256;
							NEW_TH = TL_TH/256;
							time(500);
							TR0=0;
							time(5);
							TR0=1;
					}
			}
}


//定时器实现定时翻转
void Timer_down() interrupt 1
{		
	
	
		//这里的TL和TH的初始值一定要重新定义，否则51级开发板不响
		
		TL0 = NEW_TL;		
		TH0 = NEW_TH;
		BEEP = !BEEP;
		

}

