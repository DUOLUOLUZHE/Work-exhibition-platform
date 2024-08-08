#include "head.h"


int off = 100;

void cartoon(){
		Timer0Init();
		while(off){
			button(7,0x3C);
			off--;
		}
		off = 100;
		time(100);
		P0 = 0xFF;
		while(off){
			button(6,0x3C);
			button(7,0x42);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(5,0x3C);
			button(6,0x42);
			button(7,0xA9);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(4,0x3C);
			button(5,0x42);
			button(6,0xA9);
			button(7,0x85);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(3,0x3C);
			button(4,0x42);
			button(5,0xA9);
			button(6,0x85);
			button(7,0x85);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(2,0x3C);
			button(3,0x42);
			button(4,0xA9);
			button(5,0x85);
			button(6,0x85);
			button(7,0xA9);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(1,0x3C);
			button(2,0x42);
			button(3,0xA9);
			button(4,0x85);
			button(5,0x85);
			button(6,0xA9);
			button(7,0x42);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(0,0x3C);
			button(1,0x42);
			button(2,0xA9);
			button(3,0x85);
			button(4,0x85);
			button(5,0xA9);
			button(6,0x42);
			button(7,0x3C);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(0,0x42);
			button(1,0xA9);
			button(2,0x85);
			button(3,0x85);
			button(4,0xA9);
			button(5,0x42);
			button(6,0x3C);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(0,0xA9);
			button(1,0x85);
			button(2,0x85);
			button(3,0xA9);
			button(4,0x42);
			button(5,0x3C);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(0,0x85);
			button(1,0x85);
			button(2,0xA9);
			button(3,0x42);
			button(4,0x3C);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(0,0x85);
			button(1,0xA9);
			button(2,0x42);
			button(3,0x3C);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(0,0xA9);
			button(1,0x42);
			button(2,0x3C);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(0,0x42);
			button(1,0x3C);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			button(0,0x3C);
			off--;
		}
		off = 100;
		P0 = 0xFF;
		while(off){
			time(100);
			off--;
		}
		P0 = 0xFF;
}

void clock() interrupt 1
{
	static int clo = 0;
	TL0 = 0x30;		
	TH0 = 0xF8;
	P2_1 = 0;
	clo++;
	if(clo>=500){
		clo =0;
		off = 0;
		time(100);
		off = 1;
	}


}
