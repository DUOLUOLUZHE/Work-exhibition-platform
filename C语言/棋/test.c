#define _CRT_SECURE_NO_WARNINGS test
#include "game.h"


void game() {
	char chress[X][Y] = { 0 };
	//��ʼ������
	checkerboard_relldy(chress,X,Y);
	//��ӡ����
	checkerboard_show(chress,X,Y);
	int select = 0;
	while(1) {
		//��������
		player_move(chress);
		//��ӡ����
		checkerboard_show(chress, X, Y);
		select = win(chress, SUM, X, Y);
		if (select == 1)
			break;
		//��������
		computer_move(chress,X,Y);
		//��ӡ����
		checkerboard_show(chress, X, Y);
		select = win(chress,SUM, X, Y);
		if (select == 1)
			break;
	}

}


//������Ϸ�߼�ʵ��
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




	