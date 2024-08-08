#include <REGX51.H>
#include "LCD1602.h"

int Button(int number){
	P1 = 0xFF;
	P1_3 = 0;
	if(P1_7==0){
		time(3);
		while(P1_7==0);
		time(3);
		number = 1;
	return number;
	}
	if(P1_6==0){
		time(3);
		while(P1_6==0);
		time(3);
		number = 5;
	return number;
	}
	if(P1_5==0){
		time(3);
		while(P1_5==0);
		time(3);
		number = 9;
	return number;
	}

	
	P1 = 0xFF;
	P1_2=0;
	if(P1_7==0){
		time(3);
		while(P1_7==0);
		time(3);
		number = 2;
	return number;
	}
	if(P1_6==0){
		time(3);
		while(P1_6==0);
		time(3);
		number = 6;
	return number;
	}
	if(P1_5==0){
		time(3);
		while(P1_5==0);
		time(3);
		number = 10;
	return number;
	}

	
	P1 = 0xFF;
	P1_1=0;
	if(P1_7==0){
		time(3);
		while(P1_7==0);
		time(3);
		number = 3;
	return number;
	}
	if(P1_6==0){
		time(3);
		while(P1_6==0);
		time(3);
		number = 7;
	return number;
	}
	if(P1_5==0){
		time(3);
		while(P1_5==0);
		time(3);
		number = 11;
	return number;
	}

	
	P1 = 0xFF;
	P1_0=0;
	if(P1_7==0){
		time(3);
		while(P1_7==0);
		time(3);
		number = 4;
	return number;
	}
	if(P1_6==0){
		time(3);
		while(P1_6==0);
		time(3);
		number = 8;
	return number;
	}
	if(P1_5==0){
		time(3);
		while(P1_5==0);
		time(3);
		number = 12;
		return number;
	}


}