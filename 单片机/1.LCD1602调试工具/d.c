#include <REGX51.H>
#include "LCD1602.h"

void time(){
	long sum = 30000;
	while(sum--);
}

void main(){
	while(1){
		LCD_Init();
		//LCD_ShowChar(1,1,'A');
		LCD_ShowString(1,1,"Hello,I am");
		time();
		LCD_Init();
		LCD_ShowString(1,1,"hudongyang");
		time();
		LCD_Init();
		LCD_ShowString(1,1,"one's hack");
		time();
	}
	

}