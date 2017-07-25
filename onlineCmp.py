# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import platform
import sys
import os
import time
import thread
import socket
from SSHClient import *
def get_cname_by_ip(ip_str):	
	try:
		result = socket.gethostbyaddr(ip_str)
		print "Primary hostname:"
		print " " + result[0]
		# Display the list of available addresses
		#that is also returned
		print "\nAddresses:"
		for item in result[2]:
			print " " + item
	except socket.herror, e:
		print "Couldn't look up name:", e

#通过自己的IP地址，来分析无线网段，然后查询能够ping通的结果
def get_os():
	os = platform.system()
	all_infos = platform.uname()
	if os =='Windows':
		return "n"
	else:
		return "c"

def ping_ip(ip_str):
	op=get_os()
	cmd = ["ping",'-%s'%op,"1",ip_str]
	output = os.popen(" ".join(cmd)).readlines()
	flag = False
	for line in list(output):
		if not line:
			continue
		if str(line).upper().find("TTL") >= 0:
			flag = True
			break
	if flag:
		#get_cname_by_ip(ip_str)
		#addClient(ip_str,'root','123456')
		print "[+] ip:%s is OK !!"%ip_str

def find_ip(ip_prefix): 
	''''' 
	给出当前的127.0.0 ，然后扫描整个段所有地址 
	'''
	for i in range(1,256): 
		ip = '%s.%s'%(ip_prefix,i) 
		thread.start_new_thread(ping_ip, (ip,)) 
		time.sleep(0.3) 
    
    
if __name__ == "__main__": 
  print "start time %s"%time.ctime()
  ips = map(str,sys.argv[1].split('.')[:3]);   
  find_ip('.'.join(ips)) 
  print 'Scan finished ,start to connecting .......'
  botnetCommand('uname -v')
  botnetCommand('cat /etc/issue')
  print "end time %s"%time.ctime()