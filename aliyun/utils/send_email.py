import smtplib
# 发送字符串的邮件
from email.mime.text import MIMEText
# 处理多种形态的邮件主体需要 MIMEMultipart 类
from email.mime.multipart import MIMEMultipart
# 处理图片需要 MIMEImage 类
from email.mime.image import MIMEImage


class SendEmail(object):

    def __init__(self):
        self.fromaddr = 'comgjf@163.com'  # 邮件发送方邮箱地址
        self.password = 'LWXXVMJLUFOBBEYM'  # 密码(部分邮箱为授权码)

    def send(self, toaddrs, message, subject):
        # toaddrs = ['330547543@qq.com', 'comgjf@163.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着可以写多个邮件地址群发
        # 邮件内容设置
        message = MIMEText(message, 'HTML', 'utf-8')
        # 邮件主题
        message['Subject'] = subject
        # 发送方信息
        message['From'] = self.fromaddr
        # 接受方信息
        message['To'] = toaddrs[0]
        try:
            server = smtplib.SMTP('smtp.163.com')  # 163邮箱服务器地址，端口默认为25
            server.login(self.fromaddr, self.password)
            server.sendmail(self.fromaddr, toaddrs, message.as_string())
            server.quit()
            return True
        except smtplib.SMTPException as e:
            return False
