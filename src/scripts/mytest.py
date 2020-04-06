#!/home/singhanu/anaconda3/bin/python
import sys
import getpass
print(sys.executable)

user = getpass.getuser()
if(user == "hagia-sophia"):
	print("appending path in user: %s"%(user))
	sys.path.append('/home/hagia-sophia/SchNOrb/src')
	sys.path.append('/home/hagia-sophia/schnetpack/src/schnetpack')
	work_path = "/home/hagia-sophia/orca_dft"
elif(user == "singhanu"):
	print("appending path in user: %s"%(user))
	sys.path.append('/home/singhanu/Documents/SchNOrb/src')
	work_path= "/home/singhanu/Documents/orca_dft"

import schnorb.data as data
 
print("work path %s "%(work_path))
name = []
for i in range(100):
	name.append(work_path+"/test_%d.out"%(i))



l = data.extract_basis_definition_orca([name[0]])
print(l)


print(name[0])
k = data.OrcaDataParser()

k.parse_file(name[0])


#s = data.OrcaHamiltonianParser("f1.db",l[0])
#s.parse_directories(name)