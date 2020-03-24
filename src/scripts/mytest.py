#!/usr/bin/env python
import sys
import getpass

user = getpass.getuser()
if(user == "hagia-sophia"):
	sys.path.append('/home/hagia-sophia/SchNOrb/src')
elif(user == "singhanu"):
	sys.path.append('/home/singhanu/Documents/SchNOrb/src')

import schnorb.data as data
