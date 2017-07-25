# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
pwd_folder_url = '../../sources/pwd'
from pexpect import pxssh
Found = False
def connect(host,user):
	global Found
	global result
	global err
	for filename in os.listdir(passDir):
		f = open(pwd_folder_url + filename)
		line = f.readline()
		while line:
			try:
				s = pxssh.pxssh()
				s.login(host,user,line)
				result = s
				Found = True
			except Exception, e:
				err = e
		    	line = f.readline()
		if Found:
			return result
		else:
			print '4 million pwds not enough for you !! '
			return err
	
	 
	