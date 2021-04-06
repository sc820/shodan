import shodan
import sys
from ftplib import FTP
# Configuration
API_KEY = ""

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

try:
        # Setup the api
        api = shodan.Shodan(API_KEY)
        # Perform the search
        query = "port:21 net:x.x.x.x/x"
        pagenum = 1
        count = 1

        result = api.search(query)
        while result['matches']:
            # Loop through the matches and print each IP
            for service in result['matches']:
 	        print "{}.{}".format(count,service['ip_str'])
                check_ftp(service['ip_str'])
                count += 1
            pagenum+=1
            result = api.search(query, page=pagenum)

except Exception as e:
        print 'Error: %s' % e
        sys.exit(1)

