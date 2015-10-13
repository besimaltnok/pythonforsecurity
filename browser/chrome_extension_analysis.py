__author__ = "besimaltnok"

import json
import os


extensions_path = "C:\Users\\arch\AppData\Local\Google\Chrome\User Data\Default\Extensions\\"
ext_list =  os.listdir(extensions_path)
for j in range(len(ext_list)):
    plugin_id = ext_list[j]
    manifest = os.listdir(extensions_path+plugin_id)
    if manifest is None
        pass
    else:
        full_path = extensions_path+ext_list[j] + "\\" + manifest[0] + "\\" + "manifest.json"
        with open(full_path) as data_file:
            data = json.load(data_file)
            print "Name        : %s\n" %(data['name'])
            print "Plugin id   : %s\n" %(plugin_id)
            print "Permission  : %s\n" %(data['permissions'])
            print "******************************************"


