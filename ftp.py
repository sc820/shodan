from ftplib import FTP
def check_ftp(ip):
    user="anonymous"
    passwd=""
    t=1
    try:
        ftp = FTP(ip,timeout = t)
        ftp.login(user,passwd)
        print(ip)
        print("Anonymous login successfully")
    except:
        print("Default login fail")
test_ip="127.0.0.1"
check_ftp(test_ip)

