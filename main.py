from urllib.request import urlretrieve

urlPath = 'https://s3.amazonaws.com/tcmg476/http_access_log'

logFile = 'local_copy.log'

localFile, headers = urlretrieve(urlPath, logFile)

pastSixMonths = 0
totalRequests = 0

for line in open(logFile):
    logLineInfo = line.split()
    
    if(len(logLineInfo) < 4):
        continue
    else:
        date = logLineInfo[3].split('/')
        if((date[0][1:] == '12') and (date[1] == 'Apr') and (date[2][:4] == '1995')):
            pastSixMonths += 1
    
    totalRequests += 1

print('There have been a total of %d requests over the past 6 months and %d requests in total' % (pastSixMonths, totalRequests))
