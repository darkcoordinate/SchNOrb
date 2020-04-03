#!/usr/bin/env python
import sys
import getpass
print(sys.executable)

user = getpass.getuser()
if(user == "hagia-sophia"):
	print("appending path in user: %s"%(user))
	sys.path.append('/home/hagia-sophia/SchNOrb/src')
	sys.path.append('/home/hagia-sophia/schnetpack/src/schnetpack')
elif(user == "singhanu"):
	print("appending path in user: %s"%(user))
	sys.path.append('/home/singhanu/Documents/SchNOrb/src')

import schnorb.data as data

name = []
for i in range(100):
	name.append("/home/hagia-sophia/orca_dft/test_%d.out"%(i))

l = data.extract_basis_definition_orca(name)
#print(len(l[0]))

k = data.OrcaDataParser()

k.parse_file(name[0])


#s = data.OrcaHamiltonianParser("f1.db",l[0])
#s.parse_directories(name)