#include <REGX52.H>
#include "DS1302.h"

//端口定义重命名
sbit DS1302_SCLK = P3^6;
sbit DS1302_IO = P3^4;
sbit DS1302_CE = P3^5;

//开启写保护
void DS1302_open_key(){
	DS1302_WRITE(0x8E,0x00);

}

void DS1302_Init(){
	DS1302_CE = 0;
	DS1302_SCLK = 0;

}

void DS1302_WRITE(unsigned char Command,unsigned char Data){
	unsigned char i;
	DS1302_CE = 1;
	for(i=0;i<8;i++){
		DS1302_IO = Command & 0x01;
		Command >>= 1;
		DS1302_SCLK = 1;
		
		DS1302_SCLK = 0;
	}
	for(i=0;i<8;i++){
		DS1302_IO = Data&0x01;
		Data >>= 1;
		DS1302_SCLK = 1;
		
		DS1302_SCLK = 0;
	}
	
	DS1302_CE = 0;


}

unsigned char DS1302_READ(unsigned char Command){
	unsigned char i = 0x00;
	unsigned char Data = 0x00;
	DS1302_CE = 1;
	for(i=0;i<8;i++){
		DS1302_IO = Command&(0x01<<i);
		DS1302_SCLK = 0;
		
		DS1302_SCLK = 1;
	}
	
	DS1302_IO = 0;
	
	for(i=0;i<8;i++){
		DS1302_SCLK = 1;
		
		DS1302_SCLK = 0;
		if(DS1302_IO){Data |=(0x01<<i);}
	}
	DS1302_CE = 0;
	return Data;

}