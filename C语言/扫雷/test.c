#define _CRT_SECURE_NO_WARNINGS test
#include "game.h"


//��Ϸ�߼�
int game() {
	//��������
	char chress0[X][Y] = {0};
	//���̳�ʼ��
	checkerboard_relldy0(chress0,X,Y);
	//��Ϣ������ `
	char chress_[X][Y] = {0};
	//��Ϣ�̳�ʼ��
	checkerboard_relldy_(chress_,X,Y);
	//ը��Ͷ��
	bomb(chress0, X, Y,TNT);
	printf("��ǰ��%d��%d�����̣���%d����\n",X,Y,TNT);
	while (1) {
		//��ӡ����
		//checkerboard_show(chress0, X, Y);
		//��ӡ��Ϣ��
		checkerboard_show(chress_, X, Y);
		//���ɨ��
		int select = playermove(chress0,chress_, X, Y);
		if (select == 1)
			break;
		//ʤ���ж�
		int select2 = win(chress_,TNT, X, Y);
		if (select2 == 1)
			break;
		
		
	}

	return 0;
}




//�����߼�
int main() {
	srand((unsigned int)time(NULL));
	while (1) {
		menu();
		int a = 0;
		scanf("%d", &a);
		if (a == 1) {
			printf("��Ϸ��ʼ\n");
			game();
			//break;
		}
		else if (a == 2) {
			printf("��Ϸ����\n");
			break;
		}
		else {
			printf("�Ƿ��ַ�������\n");
		}
	}
}