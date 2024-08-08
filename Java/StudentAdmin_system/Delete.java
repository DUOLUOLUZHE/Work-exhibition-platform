package StudentAdmin_system;

import java.util.ArrayList;
import java.util.Scanner;

public class Delete {
    public ArrayList<Student> delete(ArrayList<Student> list){
        Scanner s = new Scanner(System.in);
        //输入目标学号
        System.out.println("--------------------------------------");
        System.out.print("请输入想要删除的学号:");
        String student_id = s.next();

        for(int i = 0;i < list.size();i++) {
            Student stu = list.get(i);
            if(stu.STUDENT_ID.equals(student_id)){
                list.remove(i);
                System.out.println("删除成功");
                System.out.println("--------------------------------------");
                break;
            }
            if(i == list.size()-1){
                System.out.println("删除目标不存在");
                System.out.println("--------------------------------------");
                break;
            }
        }

        //id重新排序
        for(int i = 0;i < list.size();i++) {
            Student stu = list.get(i);
            stu.ID = i+1;
        }

        return list;
    }
}
