#include "head.h"

int detection(){
	if(P3_0 == 0){
		return 1;
	}else if(P3_1 == 0){
		return 2;
	}else if(P3_2 == 0){
		return 3;
	}else if(P3_3 == 0){
		return 4;
	}
	
	return 0;
	
}