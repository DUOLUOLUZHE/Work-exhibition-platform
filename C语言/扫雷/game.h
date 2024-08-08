#pragma once
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

//雷盘大小
#define X 10
#define Y 10

//炸弹数量
#define TNT 10

//打印菜单
void menu();
//雷盘初始化
void checkerboard_relldy0(char chress[X][Y], int x, int y);
//信息盘初始化
void checkerboard_relldy_(char chress[X][Y], int x, int y);
//打印信息盘
int checkerboard_show(char chress[X][Y], int x, int y);
//炸弹投放
void bomb(char chress[X][Y], int x, int y,int tnt);
//玩家扫雷
int playermove(char chress0[X][Y], char chress_[X][Y], int x, int y);
//胜利判断
int win(char chress_[X][Y],int tnt, int x, int y);

