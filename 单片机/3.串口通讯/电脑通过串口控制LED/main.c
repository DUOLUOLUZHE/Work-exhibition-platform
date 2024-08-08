#include "head.h"

void main(){
	Init();
	while(1){
		income();
	}

}

void LED() interrupt 4
{
	switch((int)SBUF){
		case 1:
			format1();
			break;
		case 2:
			format2();
			break;
		case 3:
			format3();
			break;
		case 4:
			format4();
			break;
	
	}
}