#pragma once
#include <stdio.h>
#include <string.h>

//通讯录内最大存放量
#define X 100

int start(struct number_list* one_list);
void start_number(struct number_list *one_list);

//一个人的所有信息
struct human {
	char name[20];
	int age;
	char sex[20];//man and woman
	char number[20];
	char place[40];
};

//通讯录
struct number_list {
	struct human data[X];
	//当前通讯录中数据的数量
	int number;
};