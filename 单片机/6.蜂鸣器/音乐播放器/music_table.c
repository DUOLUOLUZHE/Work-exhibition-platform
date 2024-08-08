#include <REGX52.H>
#include "music_table.h"

//C大调音符对照

//音符与索引对照表,P为休止符，L为低音M为中音，H为高音，下划线代表升半音符
#define P	0
#define L1	1
#define L1_	2
#define L2	3
#define L2_	4
#define L3	5
#define L4	6
#define L4_	7
#define L5	8
#define L5_	9
#define L6	10
#define L6_	11
#define L7	12
#define M1	13
#define M1_	14
#define M2	15
#define M2_	16
#define M3	17
#define M4	18
#define M4_	19
#define M5	20
#define M5_	21
#define M6	22
#define M6_	23
#define M7	24
#define H1	25
#define H1_	26
#define H2	27
#define H2_	28
#define H3	29
#define H4	30
#define H4_	31
#define H5	32
#define H5_	33
#define H6	34
#define H6_	35
#define H7	36


//小星星
int xiaoxingxing[] = {M1,M1,M5,M5,M6,M6,M5,M5,M4,M4,M3,M3,M2,M2,M1,M5,M5,M4,M4,M3,M3,M2,M2,M5,M5,M4,M4,M3,M3,M2,M1,M1,M5,M5,M6,M6,M5,M5,M4,M4,M3,M3,M2,M2,M1};
int xiaoxingxing_len = sizeof(xiaoxingxing) / sizeof(xiaoxingxing[0]);

int music_table(int number){
		int tl_th = 0;
		
		switch(number){
				case 0: 
				tl_th = 0; break;
        case 1: 
					tl_th = 63628; break;
        case 2: 
					tl_th = 63731; break;
        case 3: 
					tl_th = 63835; break;
        case 4: 
					tl_th = 63928; break;
        case 5: 
					tl_th = 64021; break;
        case 6: 
					tl_th = 64103; break;
        case 7: 
					tl_th = 64185; break;
        case 8: 
					tl_th = 64260; break;
        case 9: 
					tl_th = 64331; break;
        case 10: 
					tl_th = 64400; break;
        case 11: 
					tl_th = 64463; break;
        case 12: 
					tl_th = 64528; break;
        case 13: 
					tl_th = 64580; break;
        case 14: 
					tl_th = 64633; break;
        case 15: 
					tl_th = 64684; break;
        case 16: 
					tl_th = 64732; break;
        case 17: 
					tl_th = 64777; break;
        case 18: 
					tl_th = 64820; break;
        case 19: 
					tl_th = 64860; break;
        case 20: 
					tl_th = 64898; break;
        case 21: 
					tl_th = 64934; break;
        case 22: 
					tl_th = 64968; break;
        case 23: 
					tl_th = 65000; break;
        case 24: 
					tl_th = 65030; break;
        case 25: 
					tl_th = 65058; break;
        case 26: 
					tl_th = 65085; break;
        case 27: 
					tl_th = 65110; break;
        case 28: 
					tl_th = 65134; break;
        case 29: 
					tl_th = 65157; break;
        case 30: 
					tl_th = 65178; break;
        case 31: 
					tl_th = 65198; break;
        case 32: 
					tl_th = 65217; break;
        case 33: 
					tl_th = 65235; break;
        case 34: 
					tl_th = 65252; break;
        case 35: 
					tl_th = 65268; break;
        case 36: 
					tl_th = 65283; break;
		
		}
		return tl_th;

}



