#include <REGX52.H>
#include "LCD1602.h"
#include "DS1302.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>


unsigned char second,minute,hour,day,week,month,year;
unsigned char new_second,new_minute,new_hour,new_day,new_week,new_month,new_year;


//���õ�ǰʱ��

void DS1302_SetTime(){
	//���ó�ʼʱ��
	//��
	DS1302_WRITE(0x80,0x00);//����0��
	//��
	DS1302_WRITE(0x82,0x40);//����40��
	//ʱ
	DS1302_WRITE(0x84,0x03);//����3��
	//��
	DS1302_WRITE(0x86,0x14);//����14��
	//����
	DS1302_WRITE(0x8A,0x07);//��������7
	//��
	DS1302_WRITE(0x88,0x07);//��������
	//��
	DS1302_WRITE(0x8C,0x24);//����24��
	

}

void DS1302_ReadTime(){
	
	//��ȡʱ��
	//��
	second = DS1302_READ(0x81);
	//��
	minute = DS1302_READ(0x83);
	//ʱ
	hour = DS1302_READ(0x85);
	//��
	day = DS1302_READ(0x87);
	//����
	week = DS1302_READ(0x8B);
	//��
	month = DS1302_READ(0x89);
	//��
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
					//�������ģʽ
					if(off==1){
						
							while(1){
									//�ȴ�����ѡ��
									while(1){
											twice_off = new_button(0);
											if(twice_off){
												break;
											}
											
									}
									//��ʼ����
									
									//�˳�����
									if(twice_off == 1){
											break;
									}
									//ѡ�в�����λ
									if(twice_off == 2){
											//�����
											new_year = year;
											while(1){
													
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_year != year){
																//��������д��
																sprintf(hex_str, "0x%02X", new_year);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x8C,new_hex);
																
																year = new_year;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_year = (new_year/16*10 + new_year%16 + 1)/10*16 + (new_year/16*10 + new_year%16 + 1)%10;
													}
													//����
													if(third_off == 4){
															new_year = (new_year/16*10 + new_year%16 - 1)/10*16 + (new_year/16*10 + new_year%16 - 1)%10;
													}
												
													//��˸��ʾ
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
																//��������д��
																sprintf(hex_str, "0x%02X", new_year);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x8C,new_hex);
																
																year = new_year;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_year = (new_year/16*10 + new_year%16 + 1)/10*16 + (new_year/16*10 + new_year%16 + 1)%10;
													}
													//����
													if(third_off == 4){
															new_year = (new_year/16*10 + new_year%16 - 1)/10*16 + (new_year/16*10 + new_year%16 - 1)%10;
													}
													
											}
											if(third_off == 1){
													break;
											
											}
												
											
											//�µ���
											new_month = month;
											while(1){
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_month != month){
																//��������д��
																sprintf(hex_str, "0x%02X", new_month);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x88,new_hex);
																
																month = new_month;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_month = (new_month/16*10 + new_month%16 + 1)/10*16 + (new_month/16*10 + new_month%16 + 1)%10;
													}
													//����
													if(third_off == 4){
															new_month = (new_month/16*10 + new_month%16 - 1)/10*16 + (new_month/16*10 + new_month%16 - 1)%10;
													}
												
													//��˸��ʾ
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
																//��������д��
																sprintf(hex_str, "0x%02X", new_month);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x88,new_hex);
																
																month = new_month;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_month = (new_month/16*10 + new_month%16 + 1)/10*16 + (new_month/16*10 + new_month%16 + 1)%10;
													}
													//����
													if(third_off == 4){
															new_month = (new_month/16*10 + new_month%16 - 1)/10*16 + (new_month/16*10 + new_month%16 - 1)%10;
													}
													
											}
											if(third_off == 1){
													break;
											
											
											
											}
											//�յ���
											new_day = day;
											while(1){
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_day != day){
																//��������д��
																sprintf(hex_str, "0x%02X", new_day);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x86,new_hex);
																
																day = new_day;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_day = (new_day/16*10 + new_day%16 + 1)/10*16 + (new_day/16*10 + new_day%16 + 1)%10;
													}
													//����
													if(third_off == 4){
															new_day = (new_day/16*10 + new_day%16 - 1)/10*16 + (new_day/16*10 + new_day%16 - 1)%10;
													}
													
													//��˸��ʾ
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
																//��������д��
																sprintf(hex_str, "0x%02X", new_day);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x86,new_hex);
																
																day = new_day;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_day = (new_day/16*10 + new_day%16 + 1)/10*16 + (new_day/16*10 + new_day%16 + 1)%10;
													}
													//����
													if(third_off == 4){
															new_day = (new_day/16*10 + new_day%16 - 1)/10*16 + (new_day/16*10 + new_day%16 - 1)%10;
													}
													
											}
											if(third_off == 1){
													break;
											
											
											
											}
											//ʱ����
											new_hour = hour;
											while(1){
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_hour != hour){
																//��������дʱ
																sprintf(hex_str, "0x%02X", new_hour);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x84,new_hex);
																
																hour = new_hour;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_hour = (new_hour/16*10 + new_hour%16 + 1)/10*16 + (new_hour/16*10 + new_hour%16 + 1)%10;
													}
													//����
													if(third_off == 4){
															new_hour = (new_hour/16*10 + new_hour%16 - 1)/10*16 + (new_hour/16*10 + new_hour%16 - 1)%10;
													}
													
													
													//��˸��ʾ
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
																//��������дʱ
																sprintf(hex_str, "0x%02X", new_hour);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x84,new_hex);
																
																hour = new_hour;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_hour = (new_hour/16*10 + new_hour%16 + 1)/10*16 + (new_hour/16*10 + new_hour%16 + 1)%10;
													}
													//����
													if(third_off == 4){
															new_hour = (new_hour/16*10 + new_hour%16 - 1)/10*16 + (new_hour/16*10 + new_hour%16 - 1)%10;
													}
													
													
											}
											if(third_off == 1){
													break;
											
											
											
											}
											//�ֵ���
											new_minute = minute;
											while(1){
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_minute != minute){
																//��������д��
																sprintf(hex_str, "0x%02X", new_minute);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x82,new_hex);
																
																minute = new_minute;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_minute = (new_minute/16*10 + new_minute%16 + 1)/10*16 + (new_minute/16*10 + new_minute%16 + 1)%10;
													}
													//����
													if(third_off == 4){
															new_minute = (new_minute/16*10 + new_minute%16 - 1)/10*16 + (new_minute/16*10 + new_minute%16 - 1)%10;
													}
													
													
													//��˸��ʾ
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
																//��������д��
																sprintf(hex_str, "0x%02X", new_minute);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x82,new_hex);
																
																minute = new_minute;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_minute = (new_minute/16*10 + new_minute%16 + 1)/10*16 + (new_minute/16*10 + new_minute%16 + 1)%10;
													}
													//����
													if(third_off == 4){
															new_minute = (new_minute/16*10 + new_minute%16 - 1)/10*16 + (new_minute/16*10 + new_minute%16 - 1)%10;
													}
													
											if(third_off == 1){
													break;
											
											}
											
											}
											//�����
											new_second = second;
											while(1){
													third_off = new_button(0);
												
													if(third_off == 1){
															break;
													}	
												
													if(third_off == 2){
															if(new_second != second){
																//��������д��
																sprintf(hex_str, "0x%02X", new_second);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x80,new_hex);
																
																second = new_second;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_second = (new_second/16*10 + new_second%16 + 1)/10*16 + (new_second/16*10 + new_second%16 + 1)%10;
													}
													//����
													if(third_off == 4){
															new_second = (new_second/16*10 + new_second%16 - 1)/10*16 + (new_second/16*10 + new_second%16 - 1)%10;
													}
												
													//��˸��ʾ
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
																//��������д��
																sprintf(hex_str, "0x%02X", new_second);
																new_hex = (unsigned char)strtoul(hex_str, NULL, 16);
																
																DS1302_Init();
																DS1302_WRITE(0x80,new_hex);
																
																second = new_second;
															}
															break;
													}
													
													//����
													if(third_off == 3){
															new_second = (new_second/16*10 + new_second%16 + 1)/10*16 + (new_second/16*10 + new_second%16 + 1)%10;
													}
													//����
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
		
		//��ʼ��Һ����
		LCD_Init();
		LCD_ShowString(1,14,"HDY");
		//��ʼ��ʱ��ģ��
		DS1302_Init();
	
		//����ʱ��ģ��д����
		DS1302_open_key();
		//���ó�ʼʱ��
		DS1302_SetTime();
		
	
	
		while(1){
			
			//��ȡʱ��
			DS1302_ReadTime();
			
			//��ʾʱ��
			DS1302_ShowTime();
			
			//�������
			new_Button();
      
		}
		

}


