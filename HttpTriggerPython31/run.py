import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'testenv/Lib/site-packages')))

import os
import json
import platform

postreqdata = json.loads(open(os.environ['req']).read())

#print ("Python Version = '{0}'".format(platform.python_version()))

response = open(os.environ['res'], 'w')
response.write("Hello from "+postreqdata['name'])
response.close()



