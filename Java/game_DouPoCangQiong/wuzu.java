package game_DouPoCangQiong;

public class wuzu {
    //名称
    String name = "武祖";
    //血量
    int HP = 200;
    //法力
    int MP = 100;
    //变身
    private boolean OFF = true;
    //开场动画
    public void stat(){
        System.out.println("黑暗的空间崩碎，空间碎片化为洪流自虚无中冲刷而过，而在那崩塌破碎之处，一道身影踏空而来，他所过处，那等洪流竟是自动的避让开来，仿佛根本就不敢沾染上那等存在。");
        System.out.println("那等玄妙灵力，可以在冰，火，雷霆，黑暗．．．之间不断完美转换!");
        System.out.println("祂是武境之主,武祖林动！");
    }
    //技能
    public int F(int select,int role_HP){
        switch(select){
            case 1:
                if(this.OFF) {
                    System.out.println("大荒囚天指·一指囚天地！");
                    if (this.MP < 20){
                        System.out.println("武祖法力枯竭，大荒囚天指化光影溃散与天穹之上！");
                        break;
                    }
                    System.out.println("武祖造成了20点伤害！");
                    System.out.println("武祖MP-20");
                    role_HP = role_HP - 20;
                    this.MP = this.MP - 20;
                    return role_HP;
                }else{
                    System.out.println("大荒囚天指·五指动乾坤！");
                    if (this.MP < 20){
                        System.out.println("武祖法力枯竭，大荒囚天指化光影溃散与天穹之上！");
                        break;
                    }
                    System.out.println("武祖造成了40点伤害！");
                    System.out.println("武祖MP-20");
                    role_HP = role_HP - 40;
                    this.MP = this.MP - 20;
                    return role_HP;
                }

            case 2:
                if(this.OFF) {
                    System.out.println("荒芜妖眼！");
                    if (this.MP < 40){
                        System.out.println("武祖法力枯竭，诡异之气散去，荒芜妖眼重新闭合！");
                        break;
                    }
                    System.out.println("武祖造成了30点伤害！");
                    System.out.println("武祖MP-40");
                    role_HP = role_HP - 30;
                    this.MP = this.MP - 40;
                    return role_HP;

                }else{
                    System.out.println("大荒芜经·大荒芜碑！");
                    if (this.MP < 40){
                        System.out.println("武祖法力枯竭，轮回之力化擎天之手，一把收回大荒芜碑！");
                        break;
                    }
                    System.out.println("武祖造成了60点伤害！");
                    System.out.println("武祖MP-40");
                    role_HP = role_HP - 60;
                    this.MP = this.MP - 40;
                    return role_HP;
                }

            case 3:
                if(this.OFF) {
                    System.out.println("大荒囚天掌！");
                    if (this.MP < 70){
                        System.out.println("武祖法力枯竭，大荒囚天掌化光影溃散与天穹之上！");
                        break;
                    }
                    System.out.println("武祖造成了50点伤害！");
                    System.out.println("武祖MP-70");
                    role_HP = role_HP - 50;
                    this.MP = this.MP - 70;
                    return role_HP;
                }else{
                    System.out.println("八符寂灭之光！");
                    if (this.MP < 70){
                        System.out.println("武祖法力枯竭，八大祖符化流光回归武祖眉心世界！");
                        break;
                    }
                    System.out.println("武祖造成了100点伤害！");
                    System.out.println("武祖MP-70");
                    role_HP = role_HP - 100;
                    this.MP = this.MP - 70;
                    return role_HP;
                }

            case 4:
                System.out.println("吞噬祖符");
                System.out.println("武祖MP+50");
                this.MP = this.MP + 50;
                if (this.MP > 100){
                    this.MP = 100;
                }
                break;
            case 5:
                System.out.println("生死祖符");
                System.out.println("武祖HP+50");
                this.HP = this.HP + 50;
                if (this.HP > 100){
                    this.HP = 100;
                }
                break;
            case 6:
                System.out.println("青天化龙诀·青龙之气！");
                if (this.MP < 100){
                    System.out.println("武祖法力枯竭，青天化龙诀失败！");
                    break;
                }
                this.OFF = false;
                this.MP = this.MP - 100;
                break;
        }
        return role_HP;
    }
    //查看HP和MP
    public void find_see(){
        System.out.println(this.name+"当前血量"+this.HP);
        System.out.println(this.name+"当前法力值"+this.MP);

    }
}
