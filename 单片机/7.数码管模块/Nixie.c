#include <REGX52.H>
#include "time.h"

#define TIME 1


char* number_list[10]  = {0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F};


void project(int number_select,int number_math){
	
	switch(number_select){
			case 1:
				P2_4 = 0;
				P2_3 = 0;
				P2_2 = 0;
				break;
			case 2:
				P2_4 = 0;
				P2_3 = 0;
				P2_2 = 1;
				break;
			case 3:
				P2_4 = 0;
				P2_3 = 1;
				P2_2 = 0;
				break;
			case 4:
				P2_4 = 0;
				P2_3 = 1;
				P2_2 = 1;
				break;
			case 5:
				P2_4 = 1;
				P2_3 = 0;
				P2_2 = 0;
				break;
			case 6:
				P2_4 = 1;
				P2_3 = 0;
				P2_2 = 1;
				break;
			case 7:
				P2_4 = 1;
				P2_3 = 1;
				P2_2 = 0;
				break;
			case 8:
				P2_4 = 1;
				P2_3 = 1;
				P2_2 = 1;
				break;
		}
	
		P0 = *&number_list[number_math];
}



void Nixie(int a,int b,int c,int d,int e,int f,int g,int h){
	int* arr[] ={&a,&b,&c,&d,&e,&f,&g,&h};
	int i = 0;
	for(;i<8;i++){
		if(*arr[i] != 0){
			switch (i){
				case 0:
					project(8,a);
					time(TIME);
				case 1:
					project(7,b);
					time(TIME);
				case 2:
					project(6,c);
					time(TIME);
				case 3:
					project(5,d);
					time(TIME);
				case 4:
					project(4,e);
					time(TIME);
				case 5:
					project(3,f);
					time(TIME);
				case 6:
					project(2,g);
					time(TIME);
				case 7:
					project(1,h);
					time(TIME);
					i=8;
			}
		}
	}
}

void main(){
	
	while(1){
		Nixie(2,0,0,3,1,2,1,0);
	}
	
	
}