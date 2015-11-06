__author__ = "besimaltnok"

import json
import os


extensions_path = "C:\Users\\arch\AppData\Local\Google\Chrome\User Data\Default\Extensions\\"
ext_list =  os.listdir(extensions_path)
print(ext_list)
for j in range(len(ext_list)):
    plugin_id = ext_list[j]
    version = os.listdir(extensions_path+plugin_id)
    if version is not None:
        full_path = extensions_path+ext_list[j] + "\\" + version[0] + "\\" + "manifest.json"
        with open(full_path) as data_file:
            data = json.load(data_file)
            print("Name        : {}\n").format(data['name'])
            print("Plugin id   : {}\n").format(plugin_id)
            print("Permission  : {}\n").format(data['permissions'])
            print("*" * 40)
