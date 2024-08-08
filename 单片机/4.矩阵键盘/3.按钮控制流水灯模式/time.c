#include "head.h"

void init(){
	//工作模式TMOD
	TMOD = 0x01;
	//TCON配置
	TF0 = 0;
	TR0 = 1;
	//配置时间
	TH0 = 64535/256;
	TL0 = 64535%256;
	//配置中断
	ET0 = 1;
	EA = 1;
	PT0 = 0;
}

