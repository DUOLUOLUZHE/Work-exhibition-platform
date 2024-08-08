#define _CRT_SECURE_NO_WARNINGS test
#include "game.h"


//游戏逻辑
int game() {
	//雷盘数组
	char chress0[X][Y] = {0};
	//雷盘初始化
	checkerboard_relldy0(chress0,X,Y);
	//信息盘数组 `
	char chress_[X][Y] = {0};
	//信息盘初始化
	checkerboard_relldy_(chress_,X,Y);
	//炸弹投放
	bomb(chress0, X, Y,TNT);
	printf("当前是%d乘%d的棋盘，有%d个雷\n",X,Y,TNT);
	while (1) {
		//打印雷盘
		//checkerboard_show(chress0, X, Y);
		//打印信息盘
		checkerboard_show(chress_, X, Y);
		//玩家扫雷
		int select = playermove(chress0,chress_, X, Y);
		if (select == 1)
			break;
		//胜利判断
		int select2 = win(chress_,TNT, X, Y);
		if (select2 == 1)
			break;
		
		
	}

	return 0;
}




//程序逻辑
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