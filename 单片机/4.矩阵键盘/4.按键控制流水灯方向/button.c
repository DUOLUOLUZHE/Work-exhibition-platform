#include "head.h"


int button(){
	while(P2_0 == 1 && P2_1 == 1);
	if(P2_0 == 0){
		return 1;
	}
	if(P2_1 == 0){
		return 2;
	}

	return 0;
}