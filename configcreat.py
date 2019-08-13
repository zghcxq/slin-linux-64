import dlbase64


def ssr_cofig(s):
	config = {
		'server':"khabarovsk-2.abyss.moe",
		'server_ipv6': "::",
		'server_port': 30094,
		'local_address': "127.0.0.1",
		'local_port': 1080,
		'password': "D18Art",
		'method': "chacha20-ietf",
		'protocol': "auth_chain_a",
		'protocol_param': "",
		'obfs': "plain",
		'obfs_param': "",
		'speed_limit_per_con': 0,
		'speed_limit_per_user': 0,
		'additional_ports' : "{}", 
		'additional_ports_only' : "false", 
		'timeout': 120,
		'udp_timeout': 60,
		'dns_ipv6': "false",
		'connect_verbose_info': 0,
		'redirect': "",
		'fast_open': "false"
	}

	  
	spilted = s.split(':')  
	pass_param = spilted[5]
	pass_param_spilted = pass_param.split('/?')
	passwd = dlbase64.debase64_2(pass_param_spilted[0])
	passwd = passwd.decode('utf-8')

	try:
		obfs_param = re.search(r'obfsparam=([^&]+)',pass_param_spilted[1]).group[1]
	except:
		obfs_param=""
	try:
		protocol_param = re.search(r'protoparam=([^&]+)', pass_param_spilted[1])
		protocol_param = decode(protocol_param)
	except:
		protocol_param = ''
	try:
		remarks = re.search(r'remarks=([^&]+)', pass_param_spilted[1]).group(1)
		remarks = dlbase64.debase64_2(remarks)
		remarks = remarks.decode('utf-8')
	except:
		remarks = ''
	try:
		group = re.search(r'group=([^&]+)', pass_param_spilted[1]).group(1)
		group = decode(group)
	except:
		group = ''


	config['server'] = spilted[0]
	config['server_port'] = int(spilted[1])
	config['password'] = passwd
	config['method'] = spilted[3]
	config['protocol'] = spilted[2]
	config['obfs'] = spilted[4]
	config['protocol_param'] = protocol_param
	config['obfs_param'] = obfs_param

	return [config,group,remarks]



				
def vmess_config(s):


	spilted = s.split(',')  
	
	address = spilted[0].split(':') 
	alterId = spilted[1].split(':')
	alterId = alterId[1].split('\"')
	Host = spilted[2].split(':') 
	id = spilted[3].split(':') 
	network = spilted[4].split(':') 
	path = spilted[5].split(':') 
	port = spilted[6].split(':') 
	port = port[1].split('\"') 
	security = spilted[8].split(':') 
	type = spilted[9].split(':') 


	confige_file = open("config/config.json","r")
	solvethesign = len(confige_file.read())
	confige_file.close()

	confige_file = open("config/config.json", "a")
	employee_file = open("config/configmode1", "r")
	for employee in employee_file.readlines():		
		vimconfig = employee.split('#')
	vimconfig[1] = "\"address\":" +	address[1]
	vimconfig[5] = "\"alterId\":"+alterId[1]
	vimconfig[7] = "\"id\":"+id[1]
	vimconfig[9] = "\"network\":"+network[1]
	vimconfig[3] = "\"port\":"+port[1]
	vimconfig[11] = "\"security\":"+security[1]
	if  "\"tls\""==security[1]:
		vimconfig[12] = ",\"tlssettings\":{\"allowInsecure\":true,\"serverName\":\"\"}"
	if "\"ws\"" == network[1]:
		vimconfig[13] = ",\"wssettings\":{\"connectionReuse\":true,\"headers\":{"
		vimconfig[14] = "\"Host\":"+Host[1]
		vimconfig[15] = "},"
		vimconfig[16] = "\"path\":"+path[1] +"}"
	vimconfig[18] = "\"type\":"+type[1]
	configlist = []
	for numb in range(0,len(vimconfig)):	
		configlist.append(vimconfig[numb])
	resultc = ""
	solvethesameline = len(vimconfig) -1
	for configlen in range(0,solvethesameline):
		resultc= resultc + configlist[configlen]
	if solvethesign == 0:
		confige_file.write(resultc)
		print("Add vmessNode success!")
	else:	
		confige_file.write("//"+resultc)
		print("Add vmessNode success!")

	
	confige_file.close()
	employee_file.close()
		
	






