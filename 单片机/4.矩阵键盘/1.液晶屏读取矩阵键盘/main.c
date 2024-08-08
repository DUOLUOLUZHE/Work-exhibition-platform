#include <REGX51.H>
#include "LCD1602.h"

int main(){
	int number = 0;
	LCD_Init();
	LCD_ShowString(1,1,"number");
	while(1){
		//¼ì²â°´Å¥°´¶¯
		Button(&number);
		if(number){
			LCD_ShowNum(2,1,number,2);
		}
		time(3);
	}
	return 0;
}