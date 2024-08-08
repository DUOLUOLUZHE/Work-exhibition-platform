package StudentAdmin_system;

import java.util.ArrayList;
import java.util.Scanner;

public class Find {
    public void find(ArrayList<Student> list){

        //手动输入搜索信息
        Scanner s = new Scanner(System.in);
        System.out.println("--------------------------------------");
        System.out.print("请输入学号:");
        String student_id = s.next();

//        System.out.println("当前大小"+list.size());
        for(int i = 0;i < list.size();i++){
            Student stu = list.get(i);

            if(stu.STUDENT_ID.equals(student_id)){
                System.out.println("id:"+stu.ID);
                System.out.println("姓名:"+stu.NAME);
                System.out.println("年龄:"+stu.AGE);
                System.out.println("家庭住址:"+stu.FAMILY_PLACE);
                System.out.println("--------------------------------------");
                break;
            }
            if(i == list.size()-1){
                System.out.println("当前无学生信息，请添加后再查询");
                System.out.println("--------------------------------------");
                break;
            }
        }


    }
}
