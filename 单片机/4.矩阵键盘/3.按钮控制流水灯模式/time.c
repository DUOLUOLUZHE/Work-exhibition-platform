#include "head.h"

void init(){
	//����ģʽTMOD
	TMOD = 0x01;
	//TCON����
	TF0 = 0;
	TR0 = 1;
	//����ʱ��
	TH0 = 64535/256;
	TL0 = 64535%256;
	//�����ж�
	ET0 = 1;
	EA = 1;
	PT0 = 0;
}

