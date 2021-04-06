import shodan
import sys
# Configuration
API_KEY = ""
# Input validation
if len(sys.argv) == 1:
        print 'Usage: %s <search query>' % sys.argv[0]
        sys.exit(1)
try:
        # Setup the api
        api = shodan.Shodan(API_KEY)
        # Perform the search
        query = ' '.join(sys.argv[1:])
        pagenum = 1
        count = 1

        result = api.search(query)
        while result['matches']:
            # Loop through the matches and print each IP
            for service in result['matches']:
 	        print "{}.{}".format(count,service['ip_str'])
                count += 1
            pagenum+=1
            result = api.search(query, page=pagenum)

except Exception as e:
        print 'Error: %s' % e
        sys.exit(1)

