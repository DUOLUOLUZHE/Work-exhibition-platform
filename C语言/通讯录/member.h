#pragma once
#include <stdio.h>
#include <string.h>

//ͨѶ¼���������
#define X 100

int start(struct number_list* one_list);
void start_number(struct number_list *one_list);

//һ���˵�������Ϣ
struct human {
	char name[20];
	int age;
	char sex[20];//man and woman
	char number[20];
	char place[40];
};

//ͨѶ¼
struct number_list {
	struct human data[X];
	//��ǰͨѶ¼�����ݵ�����
	int number;
};