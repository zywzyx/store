def send():
    from email import encoders
    from email.header import Header
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr
    import smtplib


    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))


    from_addr = 'zywzyx_yi@163.com' #input('From: ')
    password = 'a5681631'#input('Password: ')
    to_addr = '1829225944@qq.com'#input('To: ')
    smtp_server = 'smtp.163.com'#input('SMTP server: ')

    msg = MIMEMultipart()
    msg['From'] = _format_addr('赵奕翔 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('HKR登录测试', 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('HKR登录测试', 'plain', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('F:\PythonCode\python\Auto\自动化测试\HKR登录测试.html', 'rb') as f:
        # 设置附件的MIME和文件名，这里是html类型:
        mime = MIMEBase( 'html','html', filename='HKR登录测试.html')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='HKR登录测试.html')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    with open('F:\PythonCode\python\Auto\自动化测试\loginfail.jpg', 'rb') as f:
        # 设置附件的MIME和文件名，这里是html类型:
        mime = MIMEBase('image', 'jpg', filename='loginfail.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='loginfail.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    with open('F:\PythonCode\python\Auto\自动化测试\TestCase.xlsx', 'rb') as f:
        # 设置附件的MIME和文件名，这里是html类型:
        mime = MIMEBase('xlsx', 'xlsx', filename='TestCase.xlsx')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='TestCase.xlsx')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)






    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()