#define _CRT_SECURE_NO_WARNINGS game
#include "game.h"

//��ӡѡ��˵�
void menu() {
	printf("-------------------------------\n");
	printf("----------1.��ʼ��Ϸ-----------\n");
	printf("----------2.�˳���Ϸ-----------\n");
	printf("-------------------------------\n");
	printf("-------------------------------\n");
	printf("-------------------------------\n");
	printf("��ѡ��");
}

//���̳�ʼ��
void checkerboard_relldy0(char chress[X][Y], int x, int y) {
	int i = 0;
	int j = 0;
	for (i = 0; i < x; i++) {
		for (j = 0; j < y; j++) {
			chress[i][j] = '0';
		}
	}
}
//��Ϣ�̳�ʼ��
void checkerboard_relldy_(char chress[X][Y], int x, int y) {
	int i = 0;
	int j = 0;
	for (i = 0; i < x; i++) {
		for (j = 0; j < y; j++) {
			chress[i][j] ='*';
		}
	}
}
//��ӡ����
int checkerboard_show(char chress[X][Y], int x, int y) {
	int i = 0;
	int j = 0;
	for (j = 0; j < y; j++) {
		for (i = 0; i < x; i++) {
			printf(" %c ", chress[i][j]);
			if (i < x - 1)
				printf("|");
		}
		printf("\n");
		if (j < y - 1) {
			for (i = 0; i < x; i++) {
				printf("---");
				if (i < x - 1)
					printf("|");
			}
			printf("\n");
		}
	}
	return 0;
}

//Ͷ��ը��
void bomb(char chress[X][Y], int x, int y,int tnt) {
	int i = 0;
	int xxx = 0;
	int yyy = 0;
	for (i = 0; i < tnt; i++) {
		while (1) {
			xxx = rand() % x;
			yyy = rand() % y;
			if (chress[xxx][yyy] == '0') {
				chress[xxx][yyy] = '1';
				break;
			}

		}
	}
}
//���ɨ��
int playermove(char chress0[X][Y], char chress_[X][Y], int x, int y) {
	int xx = 0;
	int yy = 0;
	
	while (1) {
		xx = 0;
		yy = 0;
		printf("���ɨ��:");
		scanf("%d %d", &xx, &yy);
		int sum = 0;
		//�ж���û��ը��
		if (chress0[xx-1][yy-1] == '1') {
			printf("game over!\n");
			return 1;
		}//�ж���û�б��¹�
		else if (chress_[xx-1][yy-1] =='*') {
			//������Ϣ
			
			if (xx-1 - 1 >= 0) {
				if (chress0[xx - 1 - 1][yy - 1] == '1') {
					sum++;
				}
			}
			if (xx + 1 -1 <= x) {
				if (chress0[xx + 1 - 1][yy - 1] == '1') {
					sum++;
				}
			}
			if (yy - 1 -1 >=0) {
				if (chress0[xx - 1][yy - 1 - 1] == '1') {
					sum++;
				}
			}
			if (yy - 1 + 1<=y) {
				if (chress0[xx - 1][yy - 1 + 1] == '1') {
					sum++;
				}
			}
			if ((xx - 1 - 1 >= 0) && (yy - 1 - 1 >=0)) {
				if (chress0[xx - 1 - 1][yy - 1 - 1] == '1') {
					sum++;
				}
			}
			if ((xx - 1 -1 >= 0) && (yy - 1 + 1<=y)) {
				if (chress0[xx - 1 - 1][yy - 1 + 1] == '1') {
					sum++;
				}
			}
			if ((xx + 1 -1<= x) && (yy - 1 - 1 >=0)) {
				if (chress0[xx + 1 - 1][yy - 1 - 1] == '1') {
					sum++;
				}
			}
			if ((xx + 1 - 1<= x) && (yy + 1 -1<=y)) {
				if (chress0[xx - 1 + 1][yy + 1 -1 ] == '1') {
					sum++;
				}
			}

			chress_[(xx - 1)][(yy - 1)] = (sum + '0');
			return 0;
		}
		else
			printf("���ﲻ���ظ�ɨ�ף�\n");
			checkerboard_show(chress_, X, Y);
	}
}

//ʤ���ж�
int win(char chress_[X][Y],int tnt,int x,int y) {
	int i = 0;
	int j = 0;
	int sum = 0;
	for (j = 0; j < y; j++) {
		for (i = 0; i < x; i++) {
			if (chress_[i][j] == '*')
				sum++;
		}
	}
	if (sum == tnt) {
		printf("��ϲɨ�׳ɹ���\n");
		return 1;
	}else
		return 0;
}
