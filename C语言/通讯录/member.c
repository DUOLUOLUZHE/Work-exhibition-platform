#define _CRT_SECURE_NO_WARNINGS member
#include "member.h"

//������ǰ
void Add(struct number_list* one_list);
int Delete(struct number_list* one_list);
int Show(struct number_list* one_list);
int Select(struct number_list* one_list);
int Amend(struct number_list* one_list);
int Sort(struct number_list* one_list, int num);

//ѡ��˵�
int start(struct number_list* one_list) {
	printf("��ӭ����ͨѶ¼����ϵͳ\n");
	while (1){
		printf("-------------------------------------------------\n");
		printf("----------------1.������ϵ��---------------------\n");
		printf("----------------2.ɾ����ϵ��---------------------\n");
		printf("----------------3.������ϵ��---------------------\n");
		printf("----------------4.�޸���ϵ����Ϣ-----------------\n");
		printf("----------------5.��ʾ������ϵ��-----------------\n");
		printf("----------------6.�˳�ϵͳ-----------------------\n");
		printf("-------------------------------------------------\n");
		printf("��ѡ��:");
		int a = 0;
		int b = 0;
		scanf("%d", &a);
		switch (a) {
			case 1:
				printf("���ӽ���\n");
				Add(&one_list);
				break;
			case 2:
				printf("ɾ������\n");
				Delete(&one_list);
				break;
			case 3:
				printf("��ʼ����\n");
				Select(&one_list);
				break;
			case 4:
				printf("�޸Ľ���\n");
				Amend(&one_list);
				break;
			case 5:
				printf("��ʼ��ʾ\n");
				Show(&one_list);
				break;
			case 6:
				printf("�˳�ϵͳ\n");
				return 0;
			default:
				printf("�Ƿ��ַ���\n");
		}
				
	}

}

//��ʼ��ͨѶ¼
void start_number(struct number_list *one_list) {
	one_list->number = 0;
	memset(one_list->data, 0, sizeof(one_list->data));
}

//����һ���û�
void Add(struct number_list* one_list) {
	printf("�����Ŀ������:");
	scanf("%s", &one_list->data[one_list->number].name);
	printf("�����Ŀ������:");
	scanf("%d", &one_list->data[one_list->number].age);
	printf("�����Ŀ���Ա�:");
	scanf("%s", &one_list->data[one_list->number].sex);
	printf("�����Ŀ��绰:");
	scanf("%s", &one_list->data[one_list->number].number);
	printf("�����Ŀ���ַ:");
	scanf("%s", &one_list->data[one_list->number].place);
	one_list->number++;
}

//ɾ��һ���û�
int Delete(struct number_list* one_list) {
	printf("��ָ��Ŀ��绰:");
	char number[20] = {0};
	scanf("%s", &number);
	int num = 0;
	for (num = 0; num <= one_list->number; num++) {
		if (num == one_list->number) {
			printf("����û�������\n");
			return 0;
		}
					

		if (strstr(one_list->data[num].number, number) != NULL) {
			memset(one_list->data[num].name, 0, sizeof(one_list->data[num].name));
			memset(one_list->data[num].number, 0, sizeof(one_list->data[num].number));
			one_list->data[num].age = 0;
			memset(one_list->data[num].sex, 0, sizeof(one_list->data[num].sex));
			memset(one_list->data[num].place, 0, sizeof(one_list->data[num].place));
			printf("ɾ���ɹ�\n");
			//�Զ�����
			Sort(&one_list,&num);
			printf("�����Զ����\n");
			one_list->number--;
			return 0;
		}
		
	}

}

//����һ���û�
int Select(struct number_list* one_list) {
	printf("��ָ��Ŀ������:");
	char name[20];
	scanf("%s", &name);
	printf("��ָ��Ŀ��绰:");
	char number[20] = {0};
	scanf("%s", &number);
	int num = 0;
	for (num = 0; num <= one_list->number; num++) {
		if (num == one_list->number) {
			printf("����û�������\n");
			return 0;
		}


		if ((strstr(one_list->data[num].number, number) != NULL) && (strstr(one_list->data[num].name , name) !=NULL)) {
			printf("--------------�û���Ϣ---------------\n");
			printf("����:%s\n", one_list->data[num].name);
			printf("����:%d\n", one_list->data[num].age);
			printf("�Ա�:%s\n", one_list->data[num].sex);
			printf("�绰:%s\n", one_list->data[num].number);
			printf("��ַ:%s\n", one_list->data[num].place);
			return 0;
		}

	}

}

//�޸�һ���û�
int Amend(struct number_list* one_list) {
	printf("��ָ��Ŀ������:");
	char name[20];
	scanf("%s", &name);
	printf("��ָ��Ŀ��绰:");
	char number[20] = { 0 };
	scanf("%s", &number);
	int num = 0;
	for (num = 0; num <= one_list->number; num++) {
		if (num == one_list->number) {
			printf("����û�������\n");
			return 0;
		}
		if ((strstr(one_list->data[num].number, number) != NULL) && (strstr(one_list->data[num].name, name) != NULL)) {
			printf("------------------��ʼ�޸�----------------\n");
			printf("���޸�Ŀ������:");
			scanf("%s", &one_list->data[num].name);
			printf("���޸�Ŀ������:");
			scanf("%d", &one_list->data[num].age);
			printf("���޸�Ŀ���Ա�:");
			scanf("%s", &one_list->data[num].sex);
			printf("���޸�Ŀ��绰:");
			scanf("%s", &one_list->data[num].number);
			printf("���޸�Ŀ���ַ:");
			scanf("%s", &one_list->data[num].place);
			return 0;
		}

	}

}

//��ʾ������ϵ����Ϣ
int Show(struct number_list* one_list) {
	int num = 0;
	for (num = 0; num < one_list->number; num++) {
		printf("---------------��%dλ----------------\n", num+1);
		printf("����:%s\n", one_list->data[num].name);
		printf("����:%d\n", one_list->data[num].age);
		printf("�Ա�:%s\n", one_list->data[num].sex);
		printf("�绰:%s\n", one_list->data[num].number);
		printf("��ַ:%s\n", one_list->data[num].place);
	}
	return 0;
}

//�Զ�����
int Sort(struct number_list* one_list,int num) {
	//�����ַ���ɾ��λ��
	strcpy(one_list->data[num].name, one_list->data[one_list->number - 1].name);
	one_list->data[num].age = one_list->data[one_list->number - 1].age;
	strcpy(one_list->data[num].sex, one_list->data[one_list->number - 1].sex);
	strcpy(one_list->data[num].number, one_list->data[one_list->number - 1].number);
	strcpy(one_list->data[num].place, one_list->data[one_list->number - 1].place);

	//��ĩβ�����������ݳ�ʼ��
	memset(one_list->data[one_list->number - 1].name, 0, sizeof(one_list->data[one_list->number - 1].name));
	one_list->data[one_list->number - 1].age = 0;
	memset(one_list->data[one_list->number - 1].sex, 0, sizeof(one_list->data[one_list->number - 1].sex));
	memset(one_list->data[one_list->number - 1].number, 0, sizeof(one_list->data[one_list->number - 1].number));
	memset(one_list->data[one_list->number - 1].place, 0, sizeof(one_list->data[one_list->number - 1].place));

	return 0;

}