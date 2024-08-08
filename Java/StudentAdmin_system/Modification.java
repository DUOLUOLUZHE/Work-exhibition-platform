package StudentAdmin_system;

import java.util.ArrayList;
import java.util.Scanner;

public class Modification {
    public ArrayList<Student> modification(ArrayList<Student> list){
        //录入欲修改学号
        System.out.println("--------------------------------------");
        System.out.print("请输入目标学号:");
        Scanner s = new Scanner(System.in);
        String student_id = s.next();


        //遍历查找，匹配修改
        for(int i = 0;i < list.size();i++) {
            Student stu = list.get(i);
            if(stu.STUDENT_ID.equals(student_id)){
                System.out.print("请输入修改后学号:");
                String Student_id = s.next();

                //判断学号唯一性

                for(int ii = 0;ii < list.size();ii++){
                    if(i!=ii) {
                        Student sstu = list.get(ii);
                        if (sstu.STUDENT_ID.equals(Student_id)) {
                            System.out.println("当前学号用户已存在，请重新操作！");
                            System.out.println("--------------------------------------");
                            return list;
                        }
                    }
                }

                stu.STUDENT_ID = Student_id;
                System.out.print("请输入修改后姓名:");
                String name = s.next();
                stu.NAME = name;
                System.out.print("请输入修改后年龄:");
                stu.AGE = s.nextInt();
                System.out.print("请输入修改后家庭住址:");
                stu.FAMILY_PLACE = s.next();
                System.out.print("修改成功！");
                System.out.println("--------------------------------------");
            }




        }
        return list;
    }
}
