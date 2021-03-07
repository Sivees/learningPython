import ldap
import datetime

ldap_server = 'ldap://alph-adds-0010.alpha.int'

connection = ldap.initialize(ldap_server)
connection.set_option(ldap.OPT_REFERRALS, 0)
connection.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
connection.set_option(ldap.OPT_X_TLS, ldap.OPT_X_TLS_DEMAND)
connection.set_option(ldap.OPT_X_TLS_DEMAND, True)
connection.set_option(ldap.OPT_DEBUG_LEVEL, 255)
connection.simple_bind_s('administrator@alpha.int', 'Pa$$w0rd')

criteria = "(&(objectClass=user)(sAMAccountName=username))"
attributes = ['displayName', 'company']

res = connection.search_s('OU=USERS,OU=ALPHA,DC=alpha,DC=int', ldap.SCOPE_SUBTREE, '(objectClass=User)')
for entry in res:
    time_string = entry[1]['whenCreated'][0].decode("utf-8").split('.')[0]
    time_created = datetime.datetime.strptime(time_string, '%Y%m%d%H%M%S')
    full_name = entry[1]['cn'][0].decode('utf-8')
    print(full_name, '-', time_created)
    # print(entry[1]['displayName'][0].decode('utf-8'))
