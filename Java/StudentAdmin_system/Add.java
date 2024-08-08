package StudentAdmin_system;
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;



public class Add {
    public ArrayList<Student> add(ArrayList<Student> list){
        //动态计算当前id值
        int id = list.size() + 1;
        //手动输入个人信息
        Scanner s = new Scanner(System.in);
        System.out.print("请输入学号:");
        String student_id = s.next();

        //判断学号唯一性
        for(int i = 0;i < list.size();i++){
            Student stu = list.get(i);
            if (stu.STUDENT_ID.equals(student_id)){
                System.out.println("当前学号用户已存在，请重新操作！");
                System.out.println("--------------------------------------");
                return list;
            }

        }


        System.out.print("请输入姓名:");
        String name = s.next();
        System.out.print("请输入年龄:");
        int age = s.nextInt();
        System.out.print("请输入家庭住址:");
        String family_place = s.next();



        Student one_member = new Student(id,student_id,name,age,family_place);
        list.add(one_member);

        return list;
    }
}
