#pragma once
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

//棋盘的长和宽
#define X 3
#define Y 3 

//几子连珠获胜
#define SUM 3


//选择菜单声明
void menu();
//初始化棋盘
void checkerboard_relldy(char chress[X][Y], int x, int y);
//打印棋盘
int checkerboard_show(char chress[X][Y],int x,int y);
//棋手下棋
void player_move(char chress[X][Y]);
//电脑下棋
void computer_move(char chress[X][Y],int x1,int y1);
//获胜判断
int win(char chress[X][Y],int sum,int x2,int y2);