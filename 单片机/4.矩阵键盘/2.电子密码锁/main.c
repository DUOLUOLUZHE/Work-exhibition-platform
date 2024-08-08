#include <REGX51.H>
#include "LCD1602.h"

//全局密码
int Password = 1234;


int main(){
	int number = 0;
	int one_data = 0;
	int sum = 0;
	LCD_Init();
	LCD_ShowString(1,1,"Password");
	while(1){
		//检测按钮按动
		one_data = Button(number);
		if(one_data == 12){
			sum = 0;
			LCD_ShowNum(2,1,sum,4);
			one_data = 0;
		}
		if(one_data == 11){
			if(Password == sum){
				LCD_ShowString(1,10,"right");
			}else{
				LCD_ShowString(1,10,"error");
			}
			one_data = 0;
		}
		if(one_data){
			if(!sum){
				sum = one_data;
			}else{
				if(sum>9999){
					one_data = 0;
				}else{
					sum = sum*10 + one_data;
					if(one_data == 10){
						sum = sum -10;
					}
				}
				
				
			}
			
		}
		if(one_data){
			LCD_ShowNum(2,1,sum,4);
		}
		one_data = 0;
		time(3);
	}
	return 0;
}