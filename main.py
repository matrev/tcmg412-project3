from urllib.request import urlretrieve

urlPath = 'https://s3.amazonaws.com/tcmg476/http_access_log'

logFile = 'local_copy.log'

localFile, headers = urlretrieve(urlPath, logFile)

for line in open(logFile):
    print(line)