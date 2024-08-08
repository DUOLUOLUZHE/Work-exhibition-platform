#include "head.h"

void time(){
	long i = 1000;
	while(i--);

}

//流水灯模式一
void format1(){
	P2_0 = 0;
	time();
	P2_0 = 1;
	P2_1 = 0;
	time();
	P2_1 = 1;
	P2_2 = 0;
	time();
	P2_2 = 1;
	P2_3 = 0;
	time();
	P2_3 = 1;
	P2_4 = 0;
	time();
	P2_4 = 1;
	P2_5 = 0;
	time();
	P2_5 = 1;
	P2_6 = 0;
	time();
	P2_6 = 1;
	P2_7 = 0;
	time();
	P2_7 = 1;
	P2_6 = 0;
	time();
	P2_6 = 1;
	P2_5 = 0;
	time();
	P2_5 = 1;
	P2_4 = 0;
	time();
	P2_4 = 1;
	P2_3 = 0;
	time();
	P2_3 = 1;
	P2_2 = 0;
	time();
	P2_2 = 1;
	P2_1 = 0;
	time();
	P2_1 = 1;
	
}

//流水灯模式二
void format2(){
	P2_0 = 0;
	P2_7 = 0;
	time();
	P2_0 = 1;
	P2_7 = 1;
	P2_1 = 0;
	P2_6 = 0;
	time();
	P2_1 = 1;
	P2_6 = 1;
	P2_2 = 0;
	P2_5 = 0;
	time();
	P2_2 = 1;
	P2_5 = 1;
	P2_3 = 0;
	P2_4 = 0;
	time();
	P2_3 = 1;
	P2_4 = 1;
	
	P2_2 = 0;
	P2_5 = 0;
	time();
	P2_2 = 1;
	P2_5 = 1;
	P2_1 = 0;
	P2_6 = 0;
	time();
	P2_1 = 1;
	P2_6 = 1;
	
	
}

//流水灯模式三
void format3(){
	P2_1 = 0;
	P2_3 = 0;
	P2_5 = 0;
	P2_7 = 0;
	time();
	P2_1 = 1;
	P2_3 = 1;
	P2_5 = 1;
	P2_7 = 1;
	P2_0 = 0;
	P2_2 = 0;
	P2_4 = 0;
	P2_6 = 0;
	time();
	P2_0 = 1;
	P2_2 = 1;
	P2_4 = 1;
	P2_6 = 1;

}

//流水灯模式四
void format4(){
	P2 = 0x00;
	time();
	P2 = 0xFF;
	time();
	
}