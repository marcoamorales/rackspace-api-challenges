'''
Write a script that creates a Cloud Database instance. This
instance should contain at least one database, and the
database should have at least one user that can
connect to it. Worth 1 Point
'''

import pyrax
import os

pyrax.set_credential_file(os.path.join(os.path.expanduser('~'),
                        '.rackspace_cloud_credentials'))

cdb = pyrax.cloud_databases
inst = cdb.create('my_db_instance', flavor='512MB Instance',
                volume=1)
print 'please wait, building instance...'
pyrax.utils.wait_until(inst, "status",
                ["ACTIVE", "ERROR"], attempts=0)
db = inst.create_database('my_first_database')
user = inst.create_user(name='myuser', password='s3cuR3p@$$w0rd',
                database_names=[db])
