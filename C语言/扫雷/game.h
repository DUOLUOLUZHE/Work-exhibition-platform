#pragma once
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

//���̴�С
#define X 10
#define Y 10

//ը������
#define TNT 10

//��ӡ�˵�
void menu();
//���̳�ʼ��
void checkerboard_relldy0(char chress[X][Y], int x, int y);
//��Ϣ�̳�ʼ��
void checkerboard_relldy_(char chress[X][Y], int x, int y);
//��ӡ��Ϣ��
int checkerboard_show(char chress[X][Y], int x, int y);
//ը��Ͷ��
void bomb(char chress[X][Y], int x, int y,int tnt);
//���ɨ��
int playermove(char chress0[X][Y], char chress_[X][Y], int x, int y);
//ʤ���ж�
int win(char chress_[X][Y],int tnt, int x, int y);

