#define _CRT_SECURE_NO_WARNINGS member
#include "member.h"

//声明提前
void Add(struct number_list* one_list);
int Delete(struct number_list* one_list);
int Show(struct number_list* one_list);
int Select(struct number_list* one_list);
int Amend(struct number_list* one_list);
int Sort(struct number_list* one_list, int num);

//选择菜单
int start(struct number_list* one_list) {
	printf("欢迎来到通讯录管理系统\n");
	while (1){
		printf("-------------------------------------------------\n");
		printf("----------------1.增加联系人---------------------\n");
		printf("----------------2.删除联系人---------------------\n");
		printf("----------------3.查找联系人---------------------\n");
		printf("----------------4.修改联系人信息-----------------\n");
		printf("----------------5.显示所有联系人-----------------\n");
		printf("----------------6.退出系统-----------------------\n");
		printf("-------------------------------------------------\n");
		printf("请选择:");
		int a = 0;
		int b = 0;
		scanf("%d", &a);
		switch (a) {
			case 1:
				printf("增加界面\n");
				Add(&one_list);
				break;
			case 2:
				printf("删除界面\n");
				Delete(&one_list);
				break;
			case 3:
				printf("开始查找\n");
				Select(&one_list);
				break;
			case 4:
				printf("修改界面\n");
				Amend(&one_list);
				break;
			case 5:
				printf("开始显示\n");
				Show(&one_list);
				break;
			case 6:
				printf("退出系统\n");
				return 0;
			default:
				printf("非法字符！\n");
		}
				
	}

}

//初始化通讯录
void start_number(struct number_list *one_list) {
	one_list->number = 0;
	memset(one_list->data, 0, sizeof(one_list->data));
}

//增加一个用户
void Add(struct number_list* one_list) {
	printf("请添加目标姓名:");
	scanf("%s", &one_list->data[one_list->number].name);
	printf("请添加目标年龄:");
	scanf("%d", &one_list->data[one_list->number].age);
	printf("请添加目标性别:");
	scanf("%s", &one_list->data[one_list->number].sex);
	printf("请添加目标电话:");
	scanf("%s", &one_list->data[one_list->number].number);
	printf("请添加目标地址:");
	scanf("%s", &one_list->data[one_list->number].place);
	one_list->number++;
}

//删除一个用户
int Delete(struct number_list* one_list) {
	printf("请指定目标电话:");
	char number[20] = {0};
	scanf("%s", &number);
	int num = 0;
	for (num = 0; num <= one_list->number; num++) {
		if (num == one_list->number) {
			printf("这个用户不存在\n");
			return 0;
		}
					

		if (strstr(one_list->data[num].number, number) != NULL) {
			memset(one_list->data[num].name, 0, sizeof(one_list->data[num].name));
			memset(one_list->data[num].number, 0, sizeof(one_list->data[num].number));
			one_list->data[num].age = 0;
			memset(one_list->data[num].sex, 0, sizeof(one_list->data[num].sex));
			memset(one_list->data[num].place, 0, sizeof(one_list->data[num].place));
			printf("删除成功\n");
			//自动排序
			Sort(&one_list,&num);
			printf("排序自动完成\n");
			one_list->number--;
			return 0;
		}
		
	}

}

//查找一个用户
int Select(struct number_list* one_list) {
	printf("请指定目标姓名:");
	char name[20];
	scanf("%s", &name);
	printf("请指定目标电话:");
	char number[20] = {0};
	scanf("%s", &number);
	int num = 0;
	for (num = 0; num <= one_list->number; num++) {
		if (num == one_list->number) {
			printf("这个用户不存在\n");
			return 0;
		}


		if ((strstr(one_list->data[num].number, number) != NULL) && (strstr(one_list->data[num].name , name) !=NULL)) {
			printf("--------------用户信息---------------\n");
			printf("姓名:%s\n", one_list->data[num].name);
			printf("年龄:%d\n", one_list->data[num].age);
			printf("性别:%s\n", one_list->data[num].sex);
			printf("电话:%s\n", one_list->data[num].number);
			printf("地址:%s\n", one_list->data[num].place);
			return 0;
		}

	}

}

//修改一个用户
int Amend(struct number_list* one_list) {
	printf("请指定目标姓名:");
	char name[20];
	scanf("%s", &name);
	printf("请指定目标电话:");
	char number[20] = { 0 };
	scanf("%s", &number);
	int num = 0;
	for (num = 0; num <= one_list->number; num++) {
		if (num == one_list->number) {
			printf("这个用户不存在\n");
			return 0;
		}
		if ((strstr(one_list->data[num].number, number) != NULL) && (strstr(one_list->data[num].name, name) != NULL)) {
			printf("------------------开始修改----------------\n");
			printf("请修改目标姓名:");
			scanf("%s", &one_list->data[num].name);
			printf("请修改目标年龄:");
			scanf("%d", &one_list->data[num].age);
			printf("请修改目标性别:");
			scanf("%s", &one_list->data[num].sex);
			printf("请修改目标电话:");
			scanf("%s", &one_list->data[num].number);
			printf("请修改目标地址:");
			scanf("%s", &one_list->data[num].place);
			return 0;
		}

	}

}

//显示所有联系人信息
int Show(struct number_list* one_list) {
	int num = 0;
	for (num = 0; num < one_list->number; num++) {
		printf("---------------第%d位----------------\n", num+1);
		printf("姓名:%s\n", one_list->data[num].name);
		printf("年龄:%d\n", one_list->data[num].age);
		printf("性别:%s\n", one_list->data[num].sex);
		printf("电话:%s\n", one_list->data[num].number);
		printf("地址:%s\n", one_list->data[num].place);
	}
	return 0;
}

//自动排序
int Sort(struct number_list* one_list,int num) {
	//拷贝字符到删除位置
	strcpy(one_list->data[num].name, one_list->data[one_list->number - 1].name);
	one_list->data[num].age = one_list->data[one_list->number - 1].age;
	strcpy(one_list->data[num].sex, one_list->data[one_list->number - 1].sex);
	strcpy(one_list->data[num].number, one_list->data[one_list->number - 1].number);
	strcpy(one_list->data[num].place, one_list->data[one_list->number - 1].place);

	//将末尾被拷贝处数据初始化
	memset(one_list->data[one_list->number - 1].name, 0, sizeof(one_list->data[one_list->number - 1].name));
	one_list->data[one_list->number - 1].age = 0;
	memset(one_list->data[one_list->number - 1].sex, 0, sizeof(one_list->data[one_list->number - 1].sex));
	memset(one_list->data[one_list->number - 1].number, 0, sizeof(one_list->data[one_list->number - 1].number));
	memset(one_list->data[one_list->number - 1].place, 0, sizeof(one_list->data[one_list->number - 1].place));

	return 0;

}