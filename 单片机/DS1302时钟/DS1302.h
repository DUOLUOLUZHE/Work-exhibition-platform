#ifndef __DS1302_H__
#define __DS1302_H__

void DS1302_open_key();
void DS1302_Init();
void time(int number);
void DS1302_WRITE(unsigned char Command,unsigned char Data);
unsigned char DS1302_READ(unsigned char Command);
int new_button(int number);


#endif
