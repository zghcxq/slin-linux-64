
# -*- coding: utf-8 -*-

import base64
import json

import configcreat 





def base64decode(s):
    transtab = str.maketrans('-_', '+/')
    s = s.translate(transtab)
    if len(s) % 4 != 0:
    	s = s + (4 - len(s) % 4)*'='
    return base64.urlsafe_b64decode(s.encode())




def decode_v2ray(vmess):
    

    
    first_b = base64decode(vmess[8:])

    configcreat.vmess_config(first_b.decode())



def decode_ssr(ssr):
    first_b = base64decode(ssr[6:])
    
    print(first_b.decode())
    config, remarks,group = configcreat.ssr_cofig(first_b.decode())
    reslt = json.dumps(config)
    
    employee_file = open("config/shadowsocks.json","r")
   
    solvethesign = len(employee_file.read())

    employee_file.close()
    if solvethesign == 0:

    	employee_file = open("config/shadowsocks.json", "w") 
    
    	employee_file.write(reslt)
    else:

    	employee_file = open("config/shadowsocks.json", "a") 
    
    	employee_file.write("//"+reslt)

    employee_file.close()
 










	






