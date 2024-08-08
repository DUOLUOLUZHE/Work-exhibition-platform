#define _CRT_SECURE_NO_WARNINGS test
#include "member.h"

int main() {
	//创建通讯录
	struct number_list one_list;
	//初始化通讯录
	start_number(&one_list);
	do {
		start(&one_list);
	} while (0);
	return 0;
}