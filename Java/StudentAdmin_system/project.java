package StudentAdmin_system;
import java.util.ArrayList;

public class project {

    public static void main(String[] args){
        //系统开关
        boolean OFF = false;
        //创建学生列表
        ArrayList<Student> list = new ArrayList<>();
        while (true) {
            //入口菜单栏
            int select = new Welcome().welcome();

            //根据用户输入选择应用
            switch (select) {
                case 1:
                    list = new Add().add(list);
                    break;
                case 2:
                    list = new Delete().delete(list);
                    break;
                case 3:
                    list = new Modification().modification(list);
                    break;
                case 4:
                    new Find().find(list);
                    break;
                case 5:
                    OFF = true;
                    break;
                default:
                    System.out.println("非法字符！");
            }

            //退出系统
            if (OFF){
                System.out.println("学员管理系统关闭");
                System.out.println("----------------------------------------");
                break;
            }
        }
    }
}
