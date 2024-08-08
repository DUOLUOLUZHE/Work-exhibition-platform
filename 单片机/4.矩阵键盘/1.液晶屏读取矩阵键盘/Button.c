#include <REGX51.H>
#include "LCD1602.h"

void Button(int * number){
	P1 = 0xFF;
	P1_3 = 0;
	if(P1_7==0){
		time(3);
		while(P1_7==0);
		time(3);
		*number = 1;
	
	}
	if(P1_6==0){
		time(3);
		while(P1_6==0);
		time(3);
		*number = 5;
	
	}
	if(P1_5==0){
		time(3);
		while(P1_5==0);
		time(3);
		*number = 9;
	
	}
	if(P1_4==0){
		time(3);
		while(P1_4==0);
		time(3);
		*number = 13;
	
	}
	
	P1 = 0xFF;
	P1_2=0;
	if(P1_7==0){
		time(3);
		while(P1_7==0);
		time(3);
		*number = 2;
	
	}
	if(P1_6==0){
		time(3);
		while(P1_6==0);
		time(3);
		*number = 6;
	
	}
	if(P1_5==0){
		time(3);
		while(P1_5==0);
		time(3);
		*number = 10;
	
	}
	if(P1_4==0){
		time(3);
		while(P1_4==0);
		time(3);
		*number = 14;
	
	}
	
	P1 = 0xFF;
	P1_1=0;
	if(P1_7==0){
		time(3);
		while(P1_7==0);
		time(3);
		*number = 3;
	
	}
	if(P1_6==0){
		time(3);
		while(P1_6==0);
		time(3);
		*number = 7;
	
	}
	if(P1_5==0){
		time(3);
		while(P1_5==0);
		time(3);
		*number = 11;
	
	}
	if(P1_4==0){
		time(3);
		while(P1_4==0);
		time(3);
		*number = 15;
	
	}
	
	P1 = 0xFF;
	P1_0=0;
	if(P1_7==0){
		time(3);
		while(P1_7==0);
		time(3);
		*number = 4;
	
	}
	if(P1_6==0){
		time(3);
		while(P1_6==0);
		time(3);
		*number = 8;
	
	}
	if(P1_5==0){
		time(3);
		while(P1_5==0);
		time(3);
		*number = 12;
	
	}
	if(P1_4==0){
		time(3);
		while(P1_4==0);
		time(3);
		*number = 16;
	
	}

}