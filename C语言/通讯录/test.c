#define _CRT_SECURE_NO_WARNINGS test
#include "member.h"

int main() {
	//����ͨѶ¼
	struct number_list one_list;
	//��ʼ��ͨѶ¼
	start_number(&one_list);
	do {
		start(&one_list);
	} while (0);
	return 0;
}