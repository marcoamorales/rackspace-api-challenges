'''
Write a script that accepts a directory as an argument as
well as a container name. The script should upload the
contents of the specified directory to the container
(or create it if it doesn't exist). The script should
handle errors appropriately. (Check for invalid paths,
etc.) 
'''

import pyrax
import os

def ask_path():
    path = raw_input('Directory: ')
    if os.path.exists(path):
        return path
    else:
        print 'Invalid directory path.'
        ask_path()

pyrax.set_credential_file(os.path.join(os.path.expanduser('~'),
                        '.rackspace_cloud_credentials'))

print '''Please type in the name of an existing container or of a new container
    to be created'''
container_name = raw_input('Container: ')
print '''Pleaes type in the path for the directory you would like to upload'''
path = ask_path()

files = [ os.path.join(path,f) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]

if container_name in pyrax.cloudfiles.list_containers():
    #container exists
    cont = pyrax.cloudfiles.get_container(container_name)
else:
    #new container
    cont = pyrax.cloudfiles.create_container(container_name)

for file in files:
    obj = cont.upload_file(file)
    if pyrax.utils.get_checksum(file) != obj.etag:
        print '[ERROR]: %s uploaded unsuccesfully' %(file)
    else:
        print ' %s uploaded successfully.' %(file)

