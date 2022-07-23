import string
import random
import json
import sys
import os

def prechecks():
	if os.getuid() != 0:
		sys.exit("PermissionError: Insufficient Permissions")
	if len(sys.argv) < 2:
		sys.exit("python3 keygen.py [keylen] [output.json]")

prechecks()

class gen:
	def key(self):
		k=""
		for i in range(int(sys.argv[1])):
			k+=random.choice(string.ascii_letters)
		return k

	def val(self):
		v=""
		for i in range(int(sys.argv[1])):
			v+=random.choice(string.ascii_letters)
		return v

def write():
	generator=gen()
	dictobj={
		
	}
	for i in range(500):
		dictobj[generator.key()]=generator.val()
	with open(sys.argv[2], "w") as j:
		content=json.dumps(dictobj, indent=4)
		j.write(content)

write()