'''
Challenge 2: Write a script that clones a server (takes an
image and deploys the image as a new server). Worth 2 Point
'''

import pyrax
import os.path import expanduser

pyrax.set_credential_file(join(expanduser('~'),'.rackspace_cloud_credentials'))

cs = pyrax.cloudservers
server1 = cs.servers.create("server1", 'da1f0392-8c64-468f-a839-a9e56caebf07', 2)
print "waiting for server to finish building..."
new_server = pyrax.utils.wait_until(server1, "status",
            ["ACTIVE", "ERROR"], attempts=0)
image_created = new_server.create_image('my test image')
image = cs.images.get(image_created)
print "waiting for image to finish building..."
new_image = pyrax.utils.wait_until(image, "status",
            ["ACTIVE", "ERROR"], attempts=0)
cloned_server = cs.servers.create("cloned server", image_created, 2)
print "waiting for cloned server to finish building"
new_cloned_server = pyrax.utils.wait_until(cloned_server, "status",
            ["ACTIVE", "ERROR"], attempts=0)
