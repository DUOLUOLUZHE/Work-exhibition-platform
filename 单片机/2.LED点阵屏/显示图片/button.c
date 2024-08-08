#include "head.h"

void button(unsigned char column,line){
	_74HC595_WriteByte(line);
	P0=~(0x80>>column);
	time(50);
	P0 = 0xFF;
}