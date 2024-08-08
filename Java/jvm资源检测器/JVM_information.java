package PC_information;

//JVM可调配资源检测

public class JVM_information {
    public static void main(String[] args){
        System.out.println("JVM可调配资源检测");
        System.out.println("------------------------------------------");
        //CPU线程检测
        System.out.println("可调配CPU线程数:"+(Runtime.getRuntime().availableProcessors()));
        //内存检测
        System.out.println("最大可调配内存:"+(Runtime.getRuntime().maxMemory()/1024/1024/1024)+"GB");
        System.out.println("已调配内存:"+(Runtime.getRuntime().totalMemory()/1024/1024)+"MB");
        System.out.println("剩余可调配内存:"+(Runtime.getRuntime().freeMemory()/1024/1024)+"MB");
    }
}
