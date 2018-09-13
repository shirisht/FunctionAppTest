import os
import json
import platform

postreqdata = json.loads(open(os.environ['req']).read())

print ("Python Version = '{0}'".format(platform.python_version()))

response = open(os.environ['res'], 'w')
response.write("Hello from "+postreqdata['name'])
response.close()
