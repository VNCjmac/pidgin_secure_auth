import json
import sys
import os

def prechecks():
	if os.getuid() != 0:
		sys.exit("PermissionError: Insufficient Permissions")
	if len(sys.argv) < 2:
		sys.exit("python3 keygen.py [authkey] [file]")

prechecks()

def resolve():
	auth=sys.argv[1]
	file=sys.argv[2]
	sear=json.loads(open(file, "r").read())
	for i,v in sear.items():
		if i == auth:
			print(f"{i} :: {v}")
			return True
	sys.exit(f"AuthError: No key matching '{auth}' was found in '{file}'")

resolve()