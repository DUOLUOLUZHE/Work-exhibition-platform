#include <REGX52.H>
#include "button.h"



int new_button(int number){
		
		if(P3_1==0){
				time(1);
				while(P3_1==0);
				time(1);
				number = 1;
				return number;
		}
		if(P3_0==0){
				time(1);
				while(P3_0==0);
				time(1);
				number = 2;
				return number;
		}
		if(P3_2==0){
				time(1);
				while(P3_2==0);
				time(1);
				number = 3;
				return number;
		}
		if(P3_3==0){
				time(1);
				while(P3_3==0);
				time(1);
				number = 4;
				return number;
		}
		return number;




}


