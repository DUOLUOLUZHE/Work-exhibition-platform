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
void checkerboard_relldy(char chress[X][Y], int x, int y) {
	int i = 0;
	int j = 0;
	for (i = 0; i < x; i++) {
		for (j = 0; j < y; j++) {
			chress[i][j] = ' ';
		}
	}
}
//��ӡ����
int checkerboard_show(char chress[X][Y], int x, int y) {
	int i = 0;
	int j = 0;
	for (j = 0; j < y;j++) {
		for (i = 0; i < x; i++) {
			printf(" %c ",chress[i][j]);
			if(i<x-1)
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
//��������
void player_move(char chress[X][Y]){
	while (1) {
		int x = 0;
		int y = 0;
		printf("��������:");
		scanf("%d %d", &x, &y);
		if (chress[x - 1][y - 1] == ' ') {
			chress[x - 1][y - 1] = '#';
			break;
		}
		else
			printf("�˴��������ӣ�\n");
	}

}
	
//��������
void computer_move(char chress[X][Y],int x1,int y1) {
	while (1) {
		int m = rand() % x1;
		int n = rand() % y1;
		if (chress[m][n] == ' ') {
			printf("��������:\n");
			chress[m][n] = '*';
			break;
		}
	}
}

//��ʤ�ж�
int win(char chress[X][Y], int sum,int x2,int y2) {
	int wind = 0;
	//�����ж�����
	int i = 0;
	int j = 0;
	int s = 0;
	for (j = 0; j < y2; j++) {
		for (i = 0; i <= x2 - sum; i++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if (chress[i + s][j] == '#')
					wind++;
			}
			if (wind == sum) {
				printf("����ʤ��\n");
					return 1;
			}
		}
		
	}
	
	//�����жϵ���
	i = 0;
	j = 0;
	s = 0;
	for (j = 0; j < y2; j++) {
		for (i = 0; i <= x2 - sum; i++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if(chress[i + s][j] == '*')
					wind++;
			}
			if (wind == sum) {
				printf("����ʤ��\n");
					return 1;
			}
		}
		
	}
	
	//�����ж�����
	i = 0;
	j = 0;
	s = 0;
	for (i = 0; i < y2; i++) {
		for (j = 0; j <= x2 - sum; j++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if(chress[i][j+s] == '#')
					wind++;
			}
			if (wind == sum) {
				printf("����ʤ��\n");
					return 1;
			}
		}
		
	}
	
	//�����жϵ���
	i = 0;
	j = 0;
	s = 0;
	for (i = 0; i < y2; i++) {
		for (j = 0; j <= x2 - sum; j++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if(chress[i][j + s] == '*')
					wind++;
			}
			if (wind == sum) {
				printf("����ʤ��\n");
					return 1;
			}
		}
		
	}

	//б���ж�����
	i = 0;
	j = 0;
	s = 0;
	for (j = 0; j < y2; j++) {
		//����б��
		for (i = 0; i < x2; i++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if (chress[i + s][j + s] == '#')
					wind++;

			}
			if (wind == sum) {
				printf("����ʤ��\n");
				return 1;
			}
		}
		//����б��
		for (i = 0; i < x2; i++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if (chress[i - s][j + s] == '#')
					wind++;

			}
			if (wind == sum) {
				printf("����ʤ��\n");
				return 1;
			}
		}
		
	}
	//б���жϵ���
	i = 0;
	j = 0;
	s = 0;
	for (j = 0; j < y2; j++) {
		//����б��
		for (i = 0; i < x2; i++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if (chress[i + s][j + s] == '*')
					wind++;

			}
			if (wind == sum) {
				printf("����ʤ��\n");
				return 1;
			}
		}
		//����б��
		for (i = 0; i < x2; i++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if (chress[i - s][j + s] == '*')
					wind++;

			}
			if (wind == sum) {
				printf("����ʤ��\n");
				return 1;
			}
		}

	}
	return 0;
}

	
		