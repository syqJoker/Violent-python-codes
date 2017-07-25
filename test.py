# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nmap import nmap
import platform
print nmap.__file__
def main():
	print platform.python_version()
	print platform.platform()
	print platform.system()
	print platform.version()
	print platform.uname()


if __name__ == '__main__':
	main()