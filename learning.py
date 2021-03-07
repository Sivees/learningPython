import socket
import yaml
import uuid
from OpenSSL import SSL

# if ip address is available
DNS_first = socket.gethostbyaddr("10.10.0.101")
# print(DNS_first)

# if domain name is available
DNS_second = socket.gethostbyname("wp.pl")
# print(DNS_second)

document = """
topaz: 1
diamond:
  alpha: "dromader"
  bravo: 4
"""

file = open('./dns.yaml', 'r')
yamlText = file.read()

# print(yamlText)

customList = yaml.load(yamlText, Loader=yaml.FullLoader)

# print(customList)
enp0s5 = 'enp0s5'
enp0s4 = 'enp0s4'
enp0s3 = 'enp0s3'
testUid = uuid.uuid4()

# print(f"uuid_v4:", testUid)
# print("")
# print(customList['alpha.int']['NS'])

srvRecords = customList['alpha.int']['SRV']
separator = '-----------------------------'
print(separator)
for rec in srvRecords:
    print(rec)
    host = srvRecords[rec]
    for a in host:
        print('   ', a)
    print(separator)
