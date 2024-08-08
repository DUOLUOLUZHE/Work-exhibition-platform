package game_DouPoCangQiong;

import java.util.Scanner;


public class master {
    private static int select;

    public static void main(String[] args){
        while (true) {
            welcome();
            if(select == 0){
                game();
            }else if(select == 1){
                break;
            }else {
                System.out.println("非法字符！");
            }
        }
    }

    public static void welcome(){
        System.out.println("-----------------------------------------");
        System.out.println("---------------决战大千世界---------------");
        System.out.println("---------------0.开始游戏-----------------");
        System.out.println("---------------1.退出游戏-----------------");
        System.out.println("-----------------------------------------");
        System.out.println("-----------------------------------------");
        System.out.println("-----------------------------------------");
        System.out.print("请输入：");
        Scanner s = new Scanner(System.in);
        select = s.nextInt();

    }
    public static int role_capacity(String name){
        System.out.println("-----------------------------------------");
        System.out.println("-----------------"+name+"------------------");
        System.out.println("---------------1-3.技能-------------------");
        System.out.println("---------------4.法力恢复-----------------");
        System.out.println("---------------5.血量恢复-----------------");
        System.out.println("---------------6.变身---------------------");
        System.out.println("-----------------------------------------");
        System.out.print("请输入：");
        Scanner s = new Scanner(System.in);
        return s.nextInt();

    }

    public static void game(){
        int i = 1;
        int sselect;
        wuzu lindong = new wuzu();
        yandi xiaoyan = new yandi();
        System.out.println("---------------------------------------------");
        System.out.println("游戏开始");
        System.out.println("---------------------------------------------");
        //登场描写
        xiaoyan.stat();
        lindong.stat();
        while (true){
            System.out.println("---------------------------------------------");
            System.out.println("第"+i+"回合");
            System.out.println("---------------------------------------------");

            //角色轮流执行操作
            sselect = role_capacity(xiaoyan.name);
            lindong.HP = xiaoyan.F(sselect,lindong.HP);

            //死亡判定
            if (lindong.HP <= 0){
                System.out.println(lindong.name+"陨落！");
                System.out.println("游戏结束");
                System.out.println("---------------------------------------------");
                break;
            }else if(xiaoyan.HP <= 0){
                System.out.println(xiaoyan.name+"陨落！");
                System.out.println("游戏结束");
                System.out.println("---------------------------------------------");
                break;
            }

            //角色轮流执行操作
            sselect = role_capacity(lindong.name);
            xiaoyan.HP = lindong.F(sselect,xiaoyan.HP);

            //死亡判定
            if (lindong.HP <= 0){
                System.out.println(lindong.name+"陨落！");
                System.out.println("游戏结束");
                System.out.println("---------------------------------------------");
                break;
            }else if(xiaoyan.HP <= 0){
                System.out.println(xiaoyan.name+"陨落！");
                System.out.println("游戏结束");
                System.out.println("---------------------------------------------");
                break;
            }

            //回合结束数据显示
            System.out.println("---------------------------------------------");
            System.out.println("第"+i+"回合结束");
            System.out.println("---------------------------------------------");

            xiaoyan.find_see();
            lindong.find_see();

            i++;
        }
    }
}
