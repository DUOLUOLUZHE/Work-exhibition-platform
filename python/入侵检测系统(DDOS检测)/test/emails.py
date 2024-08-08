import smtplib
from email.mime.text import MIMEText

class emails():
    def __init__(self):
        pass
    def start(self,data):
        # 设置服务器所需信息
        #服务器地址
        mail_host = '10.0.1.6'
        # 用户名
        mail_user = 'admin'
        # 密码(部分邮箱为授权码)
        mail_pass = 'Ygg20031210@'
        # 邮件发送方邮箱地址
        sender = 'admin@hudongyang.com'
        # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
        receivers = ['admin@hudongyang.com']
        # 设置email信息
        # 邮件内容设置
        message = MIMEText(data, 'plain', 'utf-8')
        # 邮件主题
        message['Subject'] = '入侵检测系统'
        # 发送方信息
        message['From'] = sender
        # 接受方信息
        message['To'] = receivers[0]

        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(mail_host, 25)
            # 登录到服务器
            smtpObj.login(mail_user, mail_pass)
            # 发送
            smtpObj.sendmail(
                sender, receivers, message.as_string())
            # 退出
            smtpObj.quit()
            print('发送邮件通知成功！')
        except smtplib.SMTPException as e:
            print('发送邮件通知失败！', e)


# if __name__ == '__main__':
#     data = "您的拯救者电脑正在受到DDoS攻击！！！"
#     emails = emails()
#     emails.start(data)