'''
Challenge 1: Write a script that builds three 512 MB Cloud Servers that
following a similar naming convention. (ie., web1, web2, web3) and
returns the IP and login credentials for each server. Use any image
you want. Worth 1 point
'''

import pyrax
from os.path import expanduser, join

pyrax.set_credential_file(join(expanduser("~"),".rackspace_cloud_credentials"))
cs = pyrax.cloudservers
i = 1
servers = []
while i < 4:
    servers.append(cs.servers.create('server' + str(i),
                'da1f0392-8c64-468f-a839-a9e56caebf07', 2))
    i += 1
print 'building servers... please wait'
for server in servers:
    new_srv = pyrax.utils.wait_until(server, "status",
        ["ACTIVE", "ERROR"], attempts=0)
    print 'The server %s has the user root with password %s and you can connect on IP %s.' %(server.name, server.adminPass, new_srv.networks['public'][1])
