package StudentAdmin_system;

import java.util.Scanner;



public class Welcome {
    public int welcome(){
        int select = 0;
        System.out.println("-------------欢迎来到黑马学生管理系统----------------");
        System.out.println("1：添加学生");
        System.out.println("2：删除学生");
        System.out.println("3：修改学生");
        System.out.println("4：查询学生");
        System.out.println("5：退出");
        System.out.println("请输入您的选择:");
        Scanner s = new Scanner(System.in);
        select = s.nextInt();

        return select;
    }
}
