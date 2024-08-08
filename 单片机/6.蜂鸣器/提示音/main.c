#include <REGX52.H>
#include "time.h"
#include "button.h"
#include "Nixie.h"
#include "voice.h"



int select_number = 0;


void main(){
	
	while(1){
		
		select_number = lift_button(select_number);
		
		switch(select_number){
			case 1:
				once_voice();
				select_number++;
				
				Nixie(8,1);
				
				break;
			case 2:
				
				Nixie(8,1);
				
				break;
			case 3:
				once_voice();
				select_number++;

				
				Nixie(7,2);
				
				break;
			case 4:
				
				Nixie(7,2);
				
				break;
			case 5:
				once_voice();
				select_number++;
				
				Nixie(6,3);
				
				break;
			case 6:
				
				Nixie(6,3);
				
				break;
			case 7:
				once_voice();
				select_number++;
				
				Nixie(5,4);
				
				break;
			case 8:
				
				Nixie(5,4);
				
				break;
		}
		
	}


}