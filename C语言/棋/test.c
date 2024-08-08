#define _CRT_SECURE_NO_WARNINGS test
#include "game.h"


void game() {
	char chress[X][Y] = { 0 };
	//初始化棋盘
	checkerboard_relldy(chress,X,Y);
	//打印棋盘
	checkerboard_show(chress,X,Y);
	int select = 0;
	while(1) {
		//棋手落子
		player_move(chress);
		//打印棋盘
		checkerboard_show(chress, X, Y);
		select = win(chress, SUM, X, Y);
		if (select == 1)
			break;
		//电脑落子
		computer_move(chress,X,Y);
		//打印棋盘
		checkerboard_show(chress, X, Y);
		select = win(chress,SUM, X, Y);
		if (select == 1)
			break;
	}

}


//基本游戏逻辑实现
int main() {
	srand((unsigned int)time(NULL));
	while (1) {
		menu();
		int a = 0;
		scanf("%d", &a);
		if (a == 1) {
			printf("游戏开始\n");
			game();
			//break;
		}
		else if (a == 2) {
			printf("游戏结束\n");
			break;
		}
		else {
			printf("非法字符！！！\n");
		}
	}

}




	