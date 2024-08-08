#include <REGX52.H>
#include "LCD1602.h"
#include "DS1302.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>


unsigned char second,minute,hour,day,week,month,year;
unsigned char new_second,new_minute,new_hour,new_day,new_week,new_month,new_year;


//设置当前时间

void DS1302_SetTime(){
	//设置初始时间
	//秒
	DS1302_WRITE(0x80,0x00);//代表0秒
	//分
	DS1302_WRITE(0x82,0x40);//代表40分
	//时
	DS1302_WRITE(0x84,0x03);//代表3点
	//日
	DS1302_WRITE(0x86,0x14);//代表14号
	//星期
	DS1302_WRITE(0x8A,0x07);//代表星期7
	//月
	DS1302_WRITE(0x88,0x07);//代表七月
	//年
	DS1302_WRITE(0x8C,0x24);//代表24年
	

}

void DS1302_ReadTime(){
	
	//读取时间
	//秒
	second = DS1302_READ(0x81);
	//分
	minute = DS1302_READ(0x83);
	//时
	hour = DS1302_READ(0x85);
	//日
	day = DS1302_READ(0x87);
	//星期
	week = DS1302_READ(0x8B);
	//月
	month = DS1302_READ(0x89);
	//年
	year = DS1302_READ(0x8D);
	
}



void DS1302_ShowTime(){
	LCD_ShowNum(1, 1, 20, 2);
	LCD_ShowNum(1, 3, year/16*10+year%16, 2);
	LCD_ShowString(1, 5, "-");
	LCD_ShowNum(1, 6, month/16*10+month%16, 2);
	//LCD_ShowNum(1, 7, week/16*10+week%16, 2);
	LCD_ShowString(1, 8, "-");
	LCD_ShowNum(1, 9, day/16*10+day%16, 2);
	LCD_ShowNum(2, 5, hour/16*10+hour%16, 2);
	LCD_ShowString(2, 7, ":");
	LCD_ShowNum(2, 8, minute/16*10+minute%16, 2);
	LCD_ShowString(2, 10, ":");
	LCD_ShowNum(2, 11, second/16*10+second%16, 2);


}

void new_Button(){
	
	int third_off = 0;
	int twice_off = 0;
	int off = 0;
	
	char hex_str[3];
	unsigned char new_hex;
	
	
	off = new_button(0);
	
			if(off){
					//进入调试模式
					if(off==1){
						
							while(1){
									//等待调试选择
									while(1){
											twice_off = new_button(0);
											if(twice_off){
												break;
											}
											
									}
									//开始调试
									
									//退出操作
									if(twice_off == 1){
											break;
									}
									//选中操作单位
									if(twice_off == 2){
											//年调试
											new_year = year;
											while(1){
													
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_year != year){
																//构建并重写年
																sprintf(hex_str, "0x%02X", new_year);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x8C,new_hex);
																
																year = new_year;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_year = (new_year/16*10 + new_year%16 + 1)/10*16 + (new_year/16*10 + new_year%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_year = (new_year/16*10 + new_year%16 - 1)/10*16 + (new_year/16*10 + new_year%16 - 1)%10;
													}
												
													//闪烁提示
													LCD_ShowNum(1, 1, 0, 2);
													LCD_ShowNum(1, 3, 0, 2);
													time(50);
													LCD_ShowNum(1, 1, 20, 2);
													LCD_ShowNum(1, 3, new_year/16*10+new_year%16, 2);
													time(50);
												
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_year != year){
																//构建并重写年
																sprintf(hex_str, "0x%02X", new_year);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x8C,new_hex);
																
																year = new_year;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_year = (new_year/16*10 + new_year%16 + 1)/10*16 + (new_year/16*10 + new_year%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_year = (new_year/16*10 + new_year%16 - 1)/10*16 + (new_year/16*10 + new_year%16 - 1)%10;
													}
													
											}
											if(third_off == 1){
													break;
											
											}
												
											
											//月调试
											new_month = month;
											while(1){
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_month != month){
																//构建并重写月
																sprintf(hex_str, "0x%02X", new_month);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x88,new_hex);
																
																month = new_month;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_month = (new_month/16*10 + new_month%16 + 1)/10*16 + (new_month/16*10 + new_month%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_month = (new_month/16*10 + new_month%16 - 1)/10*16 + (new_month/16*10 + new_month%16 - 1)%10;
													}
												
													//闪烁提示
													LCD_ShowNum(1, 6, 0, 2);
													time(50);
													LCD_ShowNum(1, 6, new_month/16*10+new_month%16, 2);
													time(50);
												
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_month != month){
																//构建并重写月
																sprintf(hex_str, "0x%02X", new_month);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x88,new_hex);
																
																month = new_month;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_month = (new_month/16*10 + new_month%16 + 1)/10*16 + (new_month/16*10 + new_month%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_month = (new_month/16*10 + new_month%16 - 1)/10*16 + (new_month/16*10 + new_month%16 - 1)%10;
													}
													
											}
											if(third_off == 1){
													break;
											
											
											
											}
											//日调试
											new_day = day;
											while(1){
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_day != day){
																//构建并重写日
																sprintf(hex_str, "0x%02X", new_day);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x86,new_hex);
																
																day = new_day;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_day = (new_day/16*10 + new_day%16 + 1)/10*16 + (new_day/16*10 + new_day%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_day = (new_day/16*10 + new_day%16 - 1)/10*16 + (new_day/16*10 + new_day%16 - 1)%10;
													}
													
													//闪烁提示
													LCD_ShowNum(1, 9, 0, 2);
													time(50);
													LCD_ShowNum(1, 9, new_day/16*10+new_day%16, 2);
													time(50);
												
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_day != day){
																//构建并重写日
																sprintf(hex_str, "0x%02X", new_day);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x86,new_hex);
																
																day = new_day;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_day = (new_day/16*10 + new_day%16 + 1)/10*16 + (new_day/16*10 + new_day%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_day = (new_day/16*10 + new_day%16 - 1)/10*16 + (new_day/16*10 + new_day%16 - 1)%10;
													}
													
											}
											if(third_off == 1){
													break;
											
											
											
											}
											//时调试
											new_hour = hour;
											while(1){
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_hour != hour){
																//构建并重写时
																sprintf(hex_str, "0x%02X", new_hour);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x84,new_hex);
																
																hour = new_hour;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_hour = (new_hour/16*10 + new_hour%16 + 1)/10*16 + (new_hour/16*10 + new_hour%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_hour = (new_hour/16*10 + new_hour%16 - 1)/10*16 + (new_hour/16*10 + new_hour%16 - 1)%10;
													}
													
													
													//闪烁提示
													LCD_ShowNum(2, 5, 0, 2);
													time(50);
													LCD_ShowNum(2, 5, new_hour/16*10+new_hour%16, 2);
													time(50);
												
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_hour != hour){
																//构建并重写时
																sprintf(hex_str, "0x%02X", new_hour);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x84,new_hex);
																
																hour = new_hour;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_hour = (new_hour/16*10 + new_hour%16 + 1)/10*16 + (new_hour/16*10 + new_hour%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_hour = (new_hour/16*10 + new_hour%16 - 1)/10*16 + (new_hour/16*10 + new_hour%16 - 1)%10;
													}
													
													
											}
											if(third_off == 1){
													break;
											
											
											
											}
											//分调试
											new_minute = minute;
											while(1){
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_minute != minute){
																//构建并重写分
																sprintf(hex_str, "0x%02X", new_minute);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x82,new_hex);
																
																minute = new_minute;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_minute = (new_minute/16*10 + new_minute%16 + 1)/10*16 + (new_minute/16*10 + new_minute%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_minute = (new_minute/16*10 + new_minute%16 - 1)/10*16 + (new_minute/16*10 + new_minute%16 - 1)%10;
													}
													
													
													//闪烁提示
													LCD_ShowNum(2, 8, 0, 2);
													time(50);
													LCD_ShowNum(2, 8, new_minute/16*10+new_minute%16, 2);
													time(50);
												
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_minute != minute){
																//构建并重写分
																sprintf(hex_str, "0x%02X", new_minute);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x82,new_hex);
																
																minute = new_minute;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_minute = (new_minute/16*10 + new_minute%16 + 1)/10*16 + (new_minute/16*10 + new_minute%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_minute = (new_minute/16*10 + new_minute%16 - 1)/10*16 + (new_minute/16*10 + new_minute%16 - 1)%10;
													}
													
											if(third_off == 1){
													break;
											
											}
											
											}
											//秒调试
											new_second = second;
											while(1){
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_second != second){
																//构建并重写分
																sprintf(hex_str, "0x%02X", new_second);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x80,new_hex);
																
																second = new_second;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_second = (new_second/16*10 + new_second%16 + 1)/10*16 + (new_second/16*10 + new_second%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_second = (new_second/16*10 + new_second%16 - 1)/10*16 + (new_second/16*10 + new_second%16 - 1)%10;
													}
												
													//闪烁提示
													LCD_ShowNum(2, 11, 0, 2);
													time(50);
													LCD_ShowNum(2, 11, new_second/16*10+new_second%16, 2);
													time(50);
												
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_second != second){
																//构建并重写分
																sprintf(hex_str, "0x%02X", new_second);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x80,new_hex);
																
																second = new_second;
															}
															break;
													}
													
													//增加
													if(third_off == 3){
															new_second = (new_second/16*10 + new_second%16 + 1)/10*16 + (new_second/16*10 + new_second%16 + 1)%10;
													}
													//减少
													if(third_off == 4){
															new_second = (new_second/16*10 + new_second%16 - 1)/10*16 + (new_second/16*10 + new_second%16 - 1)%10;
													}
													
											}
											if(third_off == 1){
													break;
											
											
											
											}
									
									
									}
									
									
									
									
								
							}
					}
			
			
			}

}



void main(){
		
		//初始化液晶屏
		LCD_Init();
		LCD_ShowString(1,14,"HDY");
		//初始化时间模块
		DS1302_Init();
	
		//开启时间模块写入锁
		DS1302_open_key();
		//设置初始时间
		DS1302_SetTime();
		
	
	
		while(1){
			
			//读取时间
			DS1302_ReadTime();
			
			//显示时间
			DS1302_ShowTime();
			
			//按键检测
			new_Button();
      
		}
		

}


