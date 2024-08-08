package game_DouPoCangQiong;

public class yandi {
    //名称
    String name = "炎帝";
    //血量
    int HP = 200;
    //法力
    int MP = 100;
    //开场动画
    public void stat(){
        System.out.println("某处的虚空，那里的空间在此时被撕裂开来，无穷无尽的火炎从其中呼啸出来，那种火炎，呈现极端绚丽之色，但同时，也是散发着一种令人感到惊悚的危险气息。");
        System.out.println("火海之中，一道修长人影缓步走来，他每一步的踏出，仿佛连这片空间都是在微微颤抖着，似乎是无法承受他的降临一般！");
        System.out.println("祂就是无尽火域之主,炎帝萧炎！");
    }
    //变身
    private boolean OFF = true;

    //技能
    public int F(int select,int role_HP){
        switch(select){
            case 1:
                if(this.OFF) {
                    System.out.println("焰分噬浪尺！");
                    if (this.MP < 20){
                        System.out.println("炎帝法力枯竭，焰分噬浪尺被虚空吞噬！");
                        break;
                    }
                    System.out.println("炎帝造成了20点伤害！");
                    System.out.println("炎帝MP-20");
                    role_HP = role_HP - 20;
                    this.MP = this.MP - 20;
                    return role_HP;
                }else{
                    System.out.println("炎帝·焰分噬浪尺！");
                    if (this.MP < 20){
                        System.out.println("炎帝法力枯竭，焰分噬浪尺被虚空吞噬！");
                        break;
                    }
                    System.out.println("炎帝造成了40点伤害！");
                    System.out.println("炎帝MP-20");
                    role_HP = role_HP - 40;
                    this.MP = this.MP - 20;
                    return role_HP;
                }

            case 2:
                if(this.OFF) {
                    System.out.println("大天造化掌！");
                    if (this.MP < 40){
                        System.out.println("炎帝法力枯竭，大天造化掌爆裂开来！");
                        break;
                    }
                    System.out.println("炎帝造成了30点伤害！");
                    System.out.println("炎帝MP-40");
                    role_HP = role_HP - 30;
                    this.MP = this.MP - 40;
                    return role_HP;

                }else{
                    System.out.println("炎帝·大天造化掌！");
                    if (this.MP < 40){
                        System.out.println("炎帝法力枯竭，大天造化掌爆裂开来！");
                        break;
                    }
                    System.out.println("炎帝造成了60点伤害！");
                    System.out.println("炎帝MP-40");
                    role_HP = role_HP - 60;
                    this.MP = this.MP - 40;
                    return role_HP;
                }

            case 3:
                if(this.OFF) {
                    System.out.println("佛怒火莲！");
                    if (this.MP < 70){
                        System.out.println("炎帝法力枯竭，佛怒火莲化为漫天七彩火光散去！");
                        break;
                    }
                    System.out.println("炎帝造成了50点伤害！");
                    System.out.println("炎帝MP-70");
                    role_HP = role_HP - 50;
                    this.MP = this.MP - 70;
                    return role_HP;
                }else{
                    System.out.println("异火恒古尺！");
                    if (this.MP < 70){
                        System.out.println("炎帝法力枯竭，异火恒古尺化为漫天七彩火光散去！");
                        break;
                    }
                    System.out.println("炎帝造成了100点伤害！");
                    System.out.println("炎帝MP-70");
                    role_HP = role_HP - 100;
                    this.MP = this.MP - 70;
                    return role_HP;
                }

            case 4:
                System.out.println("复灵紫丹");
                System.out.println("炎帝MP+50");
                this.MP = this.MP + 50;
                if (this.MP > 100){
                    this.MP = 100;
                }
                break;
            case 5:
                System.out.println("阴阳玄龙丹");
                System.out.println("炎帝HP+50");
                this.HP = this.HP + 50;
                if (this.HP > 100){
                    this.HP = 100;
                }
                break;
            case 6:
                System.out.println("天火三玄变·炎帝变！");
                if (this.MP < 100){
                    System.out.println("炎帝法力枯竭，天火三玄变失败！");
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
