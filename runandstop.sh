
#!/bin/bash

if [[ $1 = 'rs' ]]; 
then
	cd shadowsocks/
	sudo  python local.py -c/etc/shadowsocks.json -d start
elif [[ $1 = 'ds' ]] ;
then
	cd shadowsocks/
	sudo  python local.py -c/etc/shadowsocks.json -d stop
elif [[ $1 = 'rv' ]]; 
then
	sudo systemctl start v2ray
elif [[ $1 = 'dv' ]] ;
then
	sudo systemctl stop v2ray

elif [[ $1 = 'tv' ]] ;
then
	sudo systemctl -l|grep v2ray
fi



