#include "head.h"

sbit RCK = P3^5;
sbit SCK = P3^6;
sbit SER = P3^4;

void _74HC595_WriteByte(unsigned char Byte){
	unsigned char i;
	for(i=0;i<8;i++){
		SER = Byte&(0x80>>i);
		SCK=1;
		SCK=0;
	}
	RCK=1;
	RCK=0;
}

void main(){
	SCK=0;
	RCK=0;
	
	while(1){
		cartoon();
	}

}