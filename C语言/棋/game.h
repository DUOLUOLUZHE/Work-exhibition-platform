#pragma once
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

//���̵ĳ��Ϳ�
#define X 3
#define Y 3 

//���������ʤ
#define SUM 3


//ѡ��˵�����
void menu();
//��ʼ������
void checkerboard_relldy(char chress[X][Y], int x, int y);
//��ӡ����
int checkerboard_show(char chress[X][Y],int x,int y);
//��������
void player_move(char chress[X][Y]);
//��������
void computer_move(char chress[X][Y],int x1,int y1);
//��ʤ�ж�
int win(char chress[X][Y],int sum,int x2,int y2);