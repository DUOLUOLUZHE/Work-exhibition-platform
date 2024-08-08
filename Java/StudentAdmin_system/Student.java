package StudentAdmin_system;

public class Student {
    //成员属性
    int ID;
    String STUDENT_ID;
    String NAME;
    int AGE;
    String FAMILY_PLACE;

    //成员属性赋值
    public Student(int id,String student_id,String name,int age,String family_place){
        ID = id;
        STUDENT_ID = student_id;
        NAME = name;
        AGE = age;
        FAMILY_PLACE = family_place;
    }

    //输出姓名
    public String get_name(){
        return NAME;
    }
    //输出学号
    public String get_student_id(){
        return STUDENT_ID;
    }
    //输出年龄
    public int get_age(){
        return AGE;
    }
    //输出家庭地址
    public String get_family_place(){
        return FAMILY_PLACE;
    }


}
