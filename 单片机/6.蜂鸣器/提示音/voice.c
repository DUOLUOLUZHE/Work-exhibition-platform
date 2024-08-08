#include <REGX52.H>
#include "voice.h"
#include "time.h"

sbit BEEP = P2^5;


void once_voice(){
		int i = 500;
		while(i--){
				BEEP = !BEEP;
				time(1);
		}


}