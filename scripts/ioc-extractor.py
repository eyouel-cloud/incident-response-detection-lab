
import re, sys
data=open(sys.argv[1]).read()
ips=set(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', data))
for ip in ips: print(ip)
