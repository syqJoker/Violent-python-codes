# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pcap 
import struct
 
pack=pcap.pcap() 
pack.setfilter('udp')
key=''
for recv_time,recv_data in pack: 
	recv_len=len(recv_data)
	if recv_len == 102 and recv_data[42]== chr(02) and recv_data[101] == chr(03):
		print struct.unpack('>I',recv_data[49:53])[0]
		print '登陆了'
	elif recv_len == 55:
		print struct.unpack('>I',recv_data[49:53])[0]
		print '登陆了'