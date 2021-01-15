import configparser
from testdata.getpath import GetTestConfig
config = configparser.ConfigParser()
config.read(GetTestConfig('mail.conf'))

SMTP='SMTP'

host = config[SMTP]['host']
port = config[SMTP]['port']
user = config[SMTP]['login_user']
passwd = config[SMTP]['login_pwd']
addr = config[SMTP]['from_addr']
to_addrs = config[SMTP]['to_addrs']


print(host)
print(port)
print(user)
print(passwd)
print(addr)
print(to_addrs)