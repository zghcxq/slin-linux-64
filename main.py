import os
import sys
import dealNode
import list_node

def help():
		print ("sliny version 1.0.4  ( author:dawn)")
		print("usage: python3 main.py -h  [help] /i [init] /-s [stop]")
		print("usage: python3 main.py -N  [Node] <Node>")
		print("usage: python3 main.py -l  [list of ssrNode] |-r [run] <list> /-s [stop]")
def main():
	if len(sys.argv)==1:	
		help()
	elif len(sys.argv)==2:
		if sys.argv[1] == "-h":
			help()
		elif sys.argv[1] == "-l":
			list_node.node_list()
			
		elif sys.argv[1] == "-i":
			os.system("bash init.sh 1")
		elif sys.argv[1] == "-s":
			activev2ray = int(os.system("bash runandstop.sh tv"))
			if activev2ray == 0:
				os.system("bash runandstop.sh dv")
			os.system("bash runandstop.sh ds")	
	elif len(sys.argv)==3:
		if sys.argv[1] == "-N":
			s = sys.argv[2]
			is_ssr = s.find('ssr://')
			is_vmess = s.find('vmess://')
			if is_vmess != -1:
				vmess = s[is_vmess:].strip()
				dealNode.decode_v2ray(vmess)
			elif is_ssr != -1:
				ssr = s[is_ssr:].strip()
				
				dealNode.decode_ssr(ssr)
			else:
				print("Node is worse !!!")
		elif sys.argv[2] == "-s":
				activev2ray = int(os.system("bash runandstop.sh tv"))
				if activev2ray == 0:
					os.system("bash runandstop.sh dv")
				os.system("bash runandstop.sh ds")

	elif len(sys.argv)==4:
		if sys.argv[1] == "-l":
			if sys.argv[2] == "-r":
				activev2ray = int(os.system("bash runandstop.sh tv"))
				if activev2ray == 0:
					os.system("bash runandstop.sh dv")
				flag = list_node.choic_node(sys.argv[3])
				if flag == "ssr":
					os.system("bash runandstop.sh rs")
				if flag == "v2ray":
					os.system("bash runandstop.sh rv")
			

main()

