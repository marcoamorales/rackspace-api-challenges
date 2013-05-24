'''
Write a script that uses Cloud DNS to create a new A record
when passed a FQDN and IP address as arguments. Worth 1 Point
'''

import pyrax
import os

pyrax.set_credential_file(os.path.join(os.path.expanduser('~'),
                        '.rackspace_cloud_credentials'))


domain = pyrax.cloud_dns.create(name='my-awesome-example.com',
                    emailAddress='marco.morales@example.com')
domain.add_record([{
                    'type': 'A',
                    'name': 'example.com',
                    'data': '200.168.1.1',
                    'ttl': 6000}])
