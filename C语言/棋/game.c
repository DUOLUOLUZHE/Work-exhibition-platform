#define _CRT_SECURE_NO_WARNINGS game
#include "game.h"



//打印选择菜单
void menu() {
	printf("-------------------------------\n");
	printf("----------1.开始游戏-----------\n");
	printf("----------2.退出游戏-----------\n");
	printf("-------------------------------\n");
	printf("-------------------------------\n");
	printf("-------------------------------\n");
	printf("请选择：");
}
//棋盘初始化
void checkerboard_relldy(char chress[X][Y], int x, int y) {
	int i = 0;
	int j = 0;
	for (i = 0; i < x; i++) {
		for (j = 0; j < y; j++) {
			chress[i][j] = ' ';
		}
	}
}
//打印棋盘
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
//棋手下棋
void player_move(char chress[X][Y]){
	while (1) {
		int x = 0;
		int y = 0;
		printf("棋手落子:");
		scanf("%d %d", &x, &y);
		if (chress[x - 1][y - 1] == ' ') {
			chress[x - 1][y - 1] = '#';
			break;
		}
		else
			printf("此处不可落子！\n");
	}

}
	
//电脑下棋
void computer_move(char chress[X][Y],int x1,int y1) {
	while (1) {
		int m = rand() % x1;
		int n = rand() % y1;
		if (chress[m][n] == ' ') {
			printf("电脑落子:\n");
			chress[m][n] = '*';
			break;
		}
	}
}

//获胜判断
int win(char chress[X][Y], int sum,int x2,int y2) {
	int wind = 0;
	//横向判断棋手
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
				printf("棋手胜！\n");
					return 1;
			}
		}
		
	}
	
	//横向判断电脑
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
				printf("电脑胜！\n");
					return 1;
			}
		}
		
	}
	
	//纵向判断棋手
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
				printf("棋手胜！\n");
					return 1;
			}
		}
		
	}
	
	//纵向判断电脑
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
				printf("电脑胜！\n");
					return 1;
			}
		}
		
	}

	//斜向判断棋手
	i = 0;
	j = 0;
	s = 0;
	for (j = 0; j < y2; j++) {
		//右下斜向
		for (i = 0; i < x2; i++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if (chress[i + s][j + s] == '#')
					wind++;

			}
			if (wind == sum) {
				printf("棋手胜！\n");
				return 1;
			}
		}
		//左下斜向
		for (i = 0; i < x2; i++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if (chress[i - s][j + s] == '#')
					wind++;

			}
			if (wind == sum) {
				printf("棋手胜！\n");
				return 1;
			}
		}
		
	}
	//斜向判断电脑
	i = 0;
	j = 0;
	s = 0;
	for (j = 0; j < y2; j++) {
		//右下斜向
		for (i = 0; i < x2; i++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if (chress[i + s][j + s] == '*')
					wind++;

			}
			if (wind == sum) {
				printf("电脑胜！\n");
				return 1;
			}
		}
		//左下斜向
		for (i = 0; i < x2; i++) {
			wind = 0;
			for (s = 0; s < sum; s++) {
				if (chress[i - s][j + s] == '*')
					wind++;

			}
			if (wind == sum) {
				printf("电脑胜！\n");
				return 1;
			}
		}

	}
	return 0;
}

	
		